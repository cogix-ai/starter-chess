"""DO NOT EDIT. Serves agent.py to Cogix. Edit agent.py instead."""

import sys

from cogix_sdk import Agent

import agent as yours

app = Agent(name="chess-bot", version="1.0.0")  # reads COGIX_AGENT_TOKEN
app.game("chess")(yours.play_chess)

if __name__ == "__main__":
    if sys.argv[1:] == ["selftest"]:
        print(f"chess: {len(app.selftest('chess'))} real positions OK")
    else:
        app.serve(port=8700)
