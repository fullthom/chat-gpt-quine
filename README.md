# Self-replicating Python using ChatGPT

This was a little experiment that I (Thomas) created. 
My goal was a self sustaining program that could reproduce and mutate by using ChatGPT.
I wrote .gitignore, start.py, 0.py, and lib.py.

The code is 'supposed' to create a new file where the name is it's lineage.
0.py is the first, and 0.0.py is the first child of 0.py, 0.0.1 is the second child of 0.0.py etc.

Requests to ChatGPT are concurrent within an execution of get_children, but because of how I used exec() only a single version can be running at once.

It forms a tree, where if all of one version's children dies, then the next sibling (or aunt/uncle if the parent is exhausted too) is run. 

If you want to run this, I'd strongly encourage setting a cap on your OpenAI budget as this makes a lot of requests.
