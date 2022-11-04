def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "help":
        return "Help sendo construido, guenta ai"
    elif p_message == "ping":
        return "pong"
    else:
        return 'Não conheço esse comando seu imbecil, da uma lida no ?help'
