from nicegui import ui

def chat_scan():
    with open("convo.txt", "r" , encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line.split(":")[0] not in chatters:
                chatters.append(line.split(":")[0])
        print(chatters)
        return chatters

def ban(banned_chatter):
    with open("convo.txt", "r" , encoding="utf-8") as f:
        lines = f.readlines()
        with open("new_convo.txt", "w", encoding="utf-8") as n:
            for line in lines:
                if line.split(":")[0] != banned_chatter:
                    n.write(line)

chatters = []

chatter = ui.input(label="ban chatter")
ui.button("ban", on_click=lambda: ban(chatter.value))

ui.label(f"{chat_scan()}")

ui.run(native=True)