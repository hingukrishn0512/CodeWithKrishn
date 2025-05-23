def http_status(status):
    match status:
        case 200:
            return "ok"    
        case 404:
            return "page is not found"    
        case 500:
            return "server not found"    
        case 1000:
            return "are you out of your mind "           

        case _:
            return "abee chal na ache se server daal na" 
        
print((http_status(1000)))
print((http_status(500)))
print((http_status(200)))
print((http_status(404)))
print((http_status(401)))
