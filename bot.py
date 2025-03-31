from pypresence import Presence
import time
import random

# List of different Client IDs (Application Names)
CLIENT_IDS = {
    "1356110060069064735": "becca",  # Example: "Activity" with "becca" as cover art
    "1356110060069064735": "sucrose",  # Example: "Gaming Time" with Genshin image
    "1356110444065984694": "i_lovr_making_thesr"  # Example: "Breakcore Vibes" with FL Studio cover
}

def connect_rpc():
    """Connects to a random Discord application."""
    client_id = random.choice(list(CLIENT_IDS.keys()))  # Pick a random Client ID
    rpc = Presence(client_id)
    rpc.connect()
    return rpc, client_id, CLIENT_IDS[client_id]  # Return the selected cover art

games = [
    "Genshin Impact - TOUCH SOME GRASS",
    "With Rebecca - Go outside bro",
    "Discord Patrol - Kyaaaaaaaaa ><",
    "EMOOOOOOO - Listening to EMOO AH MUSIC"
]

i = 0  # Start with the first game

while True:
    rpc, client_id, cover_art = connect_rpc()  # Reconnect with a new Client ID & cover art
    current_game = games[i]

    rpc.update(
        details=current_game,
        large_image=cover_art,  # Custom cover art
        start=int(time.time())  # Show elapsed time
    )

    print(f"Updated status: Playing {current_game} (App: {client_id}) with cover {cover_art}")
    
    i = (i + 1) % len(games)  # Cycle through the game names
    time.sleep(10)  # Update every 10 seconds
