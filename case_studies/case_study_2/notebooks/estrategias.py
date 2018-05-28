import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import database
from snowballing.operations import reload, work_by_varname
from snowballing.snowballing import snowballing, create_provenance, log_to_provn
from copy import copy
from snowballing.models import Work
from functools import partial

gbackward = None


def todo_backward_e_depois_todo_forward(initial_set, filter_function=None):
    frontier = copy(initial_set)
    with snowballing(frontier, filter_function) as (backward, forward, log, visited):
        
        print("operacao, seed set, encontrado")
        new_frontier = frontier
        global gbackward
        gbackward = backward
        while new_frontier:
            new_frontier = backward(frontier)
            print("backward", [x.metakey for x in frontier], [x.metakey for x in new_frontier])
            frontier.update(new_frontier)
        new_frontier = frontier
        while new_frontier:
            new_frontier = forward(frontier)
            print("forward", [x.metakey for x in frontier], [x.metakey for x in new_frontier])
            frontier.update(new_frontier)
        
    return frontier, log, visited


def aplica_par_backward_forward(initial_set, filter_function=None):
    frontier = copy(initial_set)
    with snowballing(frontier, filter_function) as (backward, forward, log, visited):
        order = [backward, forward]
        new_frontier = frontier
        count = 0
        print("operacao, seed set, encontrado")
        while count < 2:
            temp = set()
            for func in order:
                count = count + 1 if not new_frontier else 0
                new_frontier = func(frontier)
                print(func.__name__, [x.metakey for x in frontier], [x.metakey for x in new_frontier])
                temp.update(new_frontier)
            frontier.update(temp)    
            
    return frontier, log, visited

alternado_a = partial(create_provenance, backward_first=True)
alternado_b = partial(create_provenance, backward_first=False)


