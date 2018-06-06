from snowballing.strategies import State

LIMIT_YEAR = None

state_visit = State.visit

def visit(self, work):
    """Visit work"""
    if LIMIT_YEAR is None or LIMIT_YEAR >= work.year:
        return state_visit(self, work)

State.visit = visit


