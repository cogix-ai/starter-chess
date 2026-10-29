"""Your Chess bot. THIS IS THE ONLY FILE YOU EDIT.

Cogix calls this once per move over HTTPS. Test offline with ./test,
run it with ./run, then follow README.md to connect it.
"""

from cogix_sdk import games


def play_chess(view):
    """Return your move. If this crashes or runs out of time, a legal move is played for you.

    view.legal_moves()   every legal move
    view.deadline_ms     your time for this move
    games.Chess(view)    .board, .turn, .in_check, ...
    """
    # TODO: your strategy. This one plays the first legal move.
    return {"kind": "move", "move": view.legal_moves()[0]}
