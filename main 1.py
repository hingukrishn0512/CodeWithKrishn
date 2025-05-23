# Complete Source Code - Rock, Paper, Scissors Game

## Project Structure
```
.
├── client/
│   └── src/
│       ├── components/
│       │   └── ui/
│       ├── hooks/
│       ├── lib/
│       ├── pages/
│       └── App.tsx
├── server/
│   ├── routes.ts
│   ├── storage.ts
│   └── db.ts
└── shared/
    └── schema.ts
```

## Frontend Source Code

### 1. Game Pages

#### `client/src/pages/welcome.tsx`:
```tsx
import { useState } from "react";
import { useLocation } from "wouter";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { motion } from "framer-motion";
import { useToast } from "@/hooks/use-toast";
import { apiRequest } from "@/lib/queryClient";
import { Hand } from "lucide-react";

const hands = ["✊", "✋", "✌️"];

export default function Welcome() {
  const [name, setName] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [, setLocation] = useLocation();
  const { toast } = useToast();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!name.trim()) {
      return toast({
        title: "Error",
        description: "Please enter your name",
        variant: "destructive",
      });
    }

    setIsLoading(true);
    try {
      const res = await apiRequest("POST", "/api/players", { name });
      const player = await res.json();
      setLocation(`/game/${player.id}`);
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to create player",
        variant: "destructive",
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen w-full flex items-center justify-center relative overflow-hidden bg-[radial-gradient(circle_at_50%_120%,rgba(120,119,198,0.3),rgba(0,0,0,0))]">
      <div className="absolute inset-0 bg-[linear-gradient(to_right,rgba(120,119,198,0.1)_1px,transparent_1px),linear-gradient(to_bottom,rgba(120,119,198,0.1)_1px,transparent_1px)] bg-[size:44px_44px]"></div>
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_0%,rgba(120,119,198,0.15),rgba(0,0,0,0))]"></div>

      <div className="absolute top-0 left-0 w-full h-48 overflow-hidden">
        {hands.map((hand, index) => (
          <motion.div
            key={index}
            className="absolute text-4xl opacity-20"
            initial={{ top: -50, left: `${index * 33}%` }}
            animate={{
              top: ["20%", "60%", "20%"],
              left: [`${index * 33}%`, `${(index * 33) + 15}%`, `${index * 33}%`],
              rotate: [0, 15, -15, 0]
            }}
            transition={{
              duration: 4,
              repeat: Infinity,
              delay: index * 0.5,
              ease: "easeInOut"
            }}
          >
            {hand}
          </motion.div>
        ))}
      </div>

      <motion.div
        initial={{ scale: 0.9, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        transition={{ duration: 0.5 }}
        className="relative"
      >
        <Card className="w-[90vw] max-w-md mx-4 border-2 border-primary/20 backdrop-blur-sm bg-background/95">
          <CardHeader className="space-y-6">
            <motion.div
              initial={{ rotate: 0 }}
              animate={{ rotate: [0, -10, 10, 0] }}
              transition={{ duration: 0.5, delay: 0.2 }}
            >
              <Hand className="w-20 h-20 mx-auto text-primary" />
            </motion.div>
            <CardTitle className="text-4xl text-center bg-gradient-to-r from-primary to-primary/60 bg-clip-text text-transparent font-bold">
              Rock, Paper, Scissors
            </CardTitle>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-6">
              <div className="space-y-2">
                <Input
                  placeholder="Enter your name"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  disabled={isLoading}
                  className="h-12 text-lg bg-background/50 backdrop-blur-sm transition-all duration-300 focus:bg-background/80"
                />
              </div>
              <motion.div
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
              >
                <Button
                  type="submit"
                  className="w-full h-12 text-lg bg-gradient-to-r from-primary to-primary/80 hover:opacity-90 transition-all duration-300"
                  disabled={isLoading}
                  size="lg"
                >
                  {isLoading ? (
                    <motion.div
                      animate={{ rotate: 360 }}
                      transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
                      className="mr-2"
                    >
                      ⭐
                    </motion.div>
                  ) : null}
                  {isLoading ? "Starting..." : "Start Game"}
                </Button>
              </motion.div>
            </form>
          </CardContent>
        </Card>
      </motion.div>
    </div>
  );
}
```

#### `client/src/pages/game.tsx`:
```tsx
import { useState } from "react";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { motion, AnimatePresence } from "framer-motion";
import { useParams, useLocation } from "wouter";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { useToast } from "@/hooks/use-toast";
import { apiRequest } from "@/lib/queryClient";
import { determineWinner, getComputerChoice } from "@/lib/game";
import type { GameChoice, GameResult, Player } from "@shared/schema";
import { Hand, Trophy, XCircle, CircleDot, Undo2, Home } from "lucide-react";

const choiceIcons = {
  rock: <Hand className="rotate-12" />,
  paper: <Hand className="-rotate-90" />,
  scissors: <Hand className="rotate-90" />
};

const resultMessages = {
  win: { title: "Victory! 🎉", color: "text-green-500" },
  lose: { title: "Defeat! 😢", color: "text-red-500" },
  tie: { title: "It's a Tie! 🤝", color: "text-yellow-500" }
};

export default function Game() {
  const { id } = useParams();
  const [, setLocation] = useLocation();
  const { toast } = useToast();
  const queryClient = useQueryClient();
  const [result, setResult] = useState<GameResult | null>(null);
  const [playerChoice, setPlayerChoice] = useState<GameChoice | null>(null);
  const [computerChoice, setComputerChoice] = useState<GameChoice | null>(null);
  const [isPlaying, setIsPlaying] = useState(false);

  const { data: player, isLoading } = useQuery<Player>({
    queryKey: [`/api/players/${id}`],
  });

  if (isLoading || !player) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-primary/20 to-primary/5">
        <div className="animate-pulse text-2xl">Loading...</div>
      </div>
    );
  }

  const makeChoice = async (choice: GameChoice) => {
    if (isPlaying) return;
    setIsPlaying(true);
    setPlayerChoice(choice);
    setComputerChoice(null);
    setResult(null);

    await new Promise(resolve => setTimeout(resolve, 800));
    const computer = getComputerChoice();
    setComputerChoice(computer);

    await new Promise(resolve => setTimeout(resolve, 400));
    const gameResult = determineWinner(choice, computer);
    setResult(gameResult);

    const newScore = player.score + (gameResult === "win" ? 1 : 0);
    try {
      await apiRequest("PATCH", `/api/players/${id}/score`, { score: newScore });
      queryClient.invalidateQueries({ queryKey: [`/api/players/${id}`] });
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to update score",
        variant: "destructive",
      });
    }

    setIsPlaying(false);
  };

  const resetGame = () => {
    setResult(null);
    setPlayerChoice(null);
    setComputerChoice(null);
  };

  return (
    <div className="min-h-screen w-full p-4 relative overflow-hidden bg-[radial-gradient(circle_at_50%_120%,rgba(120,119,198,0.3),rgba(0,0,0,0))]">
      <div className="absolute inset-0 bg-[linear-gradient(to_right,rgba(120,119,198,0.1)_1px,transparent_1px),linear-gradient(to_bottom,rgba(120,119,198,0.1)_1px,transparent_1px)] bg-[size:44px_44px]"></div>
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_0%,rgba(120,119,198,0.15),rgba(0,0,0,0))]"></div>

      <div className="relative max-w-2xl mx-auto space-y-8">
        <Card className="border-2 border-primary/20 backdrop-blur-sm bg-background/95">
          <CardHeader>
            <CardTitle className="flex items-center justify-between">
              <motion.span 
                initial={{ x: -20, opacity: 0 }}
                animate={{ x: 0, opacity: 1 }}
                className="text-2xl bg-gradient-to-r from-primary to-primary/60 bg-clip-text text-transparent"
              >
                Welcome, {player.name}!
              </motion.span>
              <motion.div 
                initial={{ scale: 0 }}
                animate={{ scale: 1 }}
                className="flex items-center gap-2 bg-primary/10 p-2 rounded-lg"
              >
                <Trophy className="w-6 h-6 text-yellow-500" />
                <span className="text-xl font-bold">{player.score}</span>
              </motion.div>
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-8">
            {/* Game Arena */}
            <div className="relative h-40 flex items-center justify-center gap-16 bg-gradient-to-b from-primary/5 to-transparent rounded-xl p-4">
              <AnimatePresence mode="wait">
                {playerChoice && (
                  <motion.div
                    initial={{ scale: 0, x: -50, rotate: -180 }}
                    animate={{ scale: 1, x: 0, rotate: 0 }}
                    exit={{ scale: 0, x: -50, rotate: 180 }}
                    className="text-5xl text-primary"
                  >
                    {choiceIcons[playerChoice]}
                  </motion.div>
                )}
              </AnimatePresence>

              {result ? (
                <motion.div
                  initial={{ scale: 0 }}
                  animate={{ scale: 1 }}
                  className={`text-2xl font-bold ${resultMessages[result].color}`}
                >
                  {resultMessages[result].title}
                </motion.div>
              ) : (
                <motion.div
                  animate={{ 
                    scale: [1, 1.1, 1],
                    opacity: [1, 0.7, 1]
                  }}
                  transition={{
                    duration: 2,
                    repeat: Infinity,
                    ease: "easeInOut"
                  }}
                  className="text-2xl font-bold text-primary/50"
                >
                  VS
                </motion.div>
              )}

              <AnimatePresence mode="wait">
                {computerChoice && (
                  <motion.div
                    initial={{ scale: 0, x: 50, rotate: 180 }}
                    animate={{ scale: 1, x: 0, rotate: 0 }}
                    exit={{ scale: 0, x: 50, rotate: -180 }}
                    className="text-5xl text-primary"
                  >
                    {choiceIcons[computerChoice]}
                  </motion.div>
                )}
              </AnimatePresence>
            </div>

            {/* Choice Buttons */}
            <div className="grid grid-cols-3 gap-4">
              {(["rock", "paper", "scissors"] as GameChoice[]).map((choice) => (
                <motion.div
                  key={choice}
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                >
                  <Button
                    onClick={() => makeChoice(choice)}
                    disabled={isPlaying}
                    className={`w-full h-24 text-lg flex flex-col items-center gap-2 transition-all duration-300 ${
                      playerChoice === choice 
                        ? "border-2 border-primary bg-primary/20" 
                        : "hover:bg-primary/10"
                    }`}
                    variant={playerChoice === choice ? "default" : "outline"}
                  >
                    {choiceIcons[choice]}
                    {choice.charAt(0).toUpperCase() + choice.slice(1)}
                  </Button>
                </motion.div>
              ))}
            </div>

            {/* Game Controls */}
            <div className="flex justify-center gap-4">
              <Button
                onClick={resetGame}
                variant="outline"
                className="w-32 transition-all duration-300 hover:bg-primary/10"
                disabled={!result}
              >
                <Undo2 className="w-4 h-4 mr-2" />
                Again
              </Button>
              <Button
                onClick={() => setLocation("/")}
                variant="outline"
                className="w-32 transition-all duration-300 hover:bg-primary/10"
              >
                <Home className="w-4 h-4 mr-2" />
                Exit
              </Button>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}


### 2. Game Logic

#### `client/src/lib/game.ts`:

import type { GameChoice, GameResult } from "@shared/schema";

export function determineWinner(
  playerChoice: GameChoice,
  computerChoice: GameChoice
): GameResult {
  if (playerChoice === computerChoice) return "tie";

  const winConditions: Record<GameChoice, GameChoice> = {
    rock: "scissors",
    paper: "rock",
    scissors: "paper",
  };

  return winConditions[playerChoice] === computerChoice ? "win" : "lose";
}

export function getComputerChoice(): GameChoice {
  const choices: GameChoice[] = ["rock", "paper", "scissors"];
  return choices[Math.floor(Math.random() * choices.length)];
}
```

### 3. Database and Types

#### `shared/schema.ts`:

import { pgTable, text, serial, integer } from "drizzle-orm/pg-core";
import { createInsertSchema } from "drizzle-zod";
import { z } from "zod";

export const players = pgTable("players", {
  id: serial("id").primaryKey(),
  name: text("name").notNull(),
  score: integer("score").notNull().default(0),
});

export const insertPlayerSchema = createInsertSchema(players).pick({
  name: true,
});

export type InsertPlayer = z.infer<typeof insertPlayerSchema>;
export type Player = typeof players.$inferSelect;

export type GameChoice = "rock" | "paper" | "scissors";
export type GameResult = "win" | "lose" | "tie";
```

### 4. Server Implementation

#### `server/routes.ts`:

import type { Express } from "express";
import { storage } from "./storage";
import { insertPlayerSchema } from "@shared/schema";

export function registerRoutes(app: Express) {
  app.post("/api/players", async (req, res) => {
    const result = insertPlayerSchema.safeParse(req.body);
    if (!result.success) {
      return res.status(400).json({ message: "Invalid player data" });
    }

    const player = await storage.createPlayer(result.data);
    res.json(player);
  });

  app.get("/api/players/:id", async (req, res) => {
    const id = parseInt(req.params.id);
    const player = await storage.getPlayer(id);
    if (!player) {
      return res.status(404).json({ message: "Player not found" });
    }
    res.json(player);
  });

  app.patch("/api/players/:id/score", async (req, res) => {
    const id = parseInt(req.params.id);
    const score = req.body.score;
    
    if (typeof score !== "number") {
      return res.status(400).json({ message: "Invalid score" });
    }

    const player = await storage.updateScore(id, score);
    res.json(player);
  });
}


#### `server/storage.ts`:

import { type Player, type InsertPlayer, players } from "@shared/schema";
import { db } from "./db";
import { eq } from "drizzle-orm";

export interface IStorage {
  getPlayer(id: number): Promise<Player | undefined>;
  createPlayer(player: InsertPlayer): Promise<Player>;
  updateScore(id: number, score: number): Promise<Player>;
}

export class DatabaseStorage implements IStorage {
  async getPlayer(id: number): Promise<Player | undefined> {
    const [player] = await db.select().from(players).where(eq(players.id, id));
    return player;
  }

  async createPlayer(insertPlayer: InsertPlayer): Promise<Player> {
    const [player] = await db
      .insert(players)
      .values(insertPlayer)
      .returning();
    return player;
  }

  async updateScore(id: number, score: number): Promise<Player> {
    const [player] = await db
      .update(players)
      .set({ score })
      .where(eq(players.id, id))
      .returning();

    if (!player) {
      throw new Error("Player not found");
    }

    return player;
  }
}

export const storage = new DatabaseStorage();

#### `server/db.ts`:

import { Pool, neonConfig } from '@neondatabase/serverless';
import { drizzle } from 'drizzle-orm/neon-serverless';
import ws from "ws";
import * as schema from "@shared/schema";

neonConfig.webSocketConstructor = ws;

if (!process.env.DATABASE_URL) {
  throw new Error(
    "DATABASE_URL must be set. Did you forget to provision a database?",
  );
}
