input = str(input("say dataname: "))
if input.find(".") != -1 and input.count(".") == 1 :
    match input.strip().lower().split(".")[1]:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
             print("application/octet-stream")
elif input.count(".") > 1:
     match input.strip().lower().split(".")[2]:
         case "gif":
            print("image/gif")
         case "jpg" | "jpeg":
            print("image/jpeg")
         case "png":
            print("image/png")
         case "pdf":
            print("application/pdf")
         case "txt":
            print("text/plain")
         case "zip":
            print("application/zip")
         case _:
            print("application/octet-stream")
else:
    print("application/octet-stream")
