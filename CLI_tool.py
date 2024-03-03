import click

# Create a new command line interface (CLI) app
@click.group()
@click.pass_context
def todo(ctx):
    # Initialize an empty dictionary in the context
    ctx.ensure_object(dict)
    # Open the 'todo.txt' file and store its contents
    with open('todo.txt') as f:
        content = f.readlines()
    # Set the latest task ID and the task list using the contents
    ctx.obj['LATEST'] = int(content[0])
    ctx.obj['TASKS'] = {
        en.split('```\n\n')[0]: en.split('```\n\n')[1][:-1]
        for en in content[1:]
    }

# Define a 'tasks' command to display the tasks
@todo.command()
@click.pass_context
def tasks(ctx):
    if ctx.obj['TASKS']:
        click.echo('YOUR TASKS\n**********')
        # Iterate through the tasks and display them
        for i, task in ctx.obj['TASKS'].items():
            click.echo('• ' + task + ' (ID: ' + i + ')')
        click.echo('')
    else:
        click.echo('No tasks yet! Use ADD to add one.\n')

# Define an 'add' command to add a new task
@todo.command()
@click.pass_context
@click.option('-add', '--add_task', prompt='Enter task to add')
def add(ctx, add_task):
    if add_task:
        # Add the new task to the task list in the context
        ctx.obj['TASKS'][ctx.obj['LATEST']] = add_task
        click.echo('Added task "' + add_task + '" with ID ' + str(ctx.obj['LATEST']))
        # Write the updated task list to 'todo.txt'
        curr_ind = [str(ctx.obj['LATEST'] + 1)] 
        tasks = [str(i) + '```\n' + t for (i, t) in ctx.obj['TASKS'].items()]
        with open('todo.txt', 'w') as f:
            f.writelines(['%s\n' % en for en in curr_ind + tasks])

# Define a 'done' command to mark a task as finished and remove it
@todo.command()
@click.pass_context
@click.option('-fin', '--fin_taskid', prompt='Enter ID of task to finish', type=int)
def done(ctx, fin_taskid):
    # Find the task with the given ID
    if str(fin_taskid) in ctx.obj['TASKS'].keys():
        task = ctx.obj['TASKS'][str(fin_taskid)]
        # Remove the task from the task list in the context
        del ctx.obj['TASKS'][str(fin_taskid)]
        click.echo('Finished and removed task "' + task + '" with id ' + str(fin_taskid))
        # Write the updated task list to 'todo.txt'
        if ctx.obj['TASKS']:
            curr_ind = [str(ctx.obj['LATEST'] + 1)] 
            tasks = [str(i) + '```\n' + t for (i, t) in ctx.obj['TASKS'].items()]
            with open('todo.txt', 'w') as f:
                f.writelines(['%s\n' % en for en in curr_ind + tasks])
        else:
            # Reset the ID tracker to 0 if the task list is empty
            with open('todo.txt', 'w') as f:
                f.writelines(['0\n'])
    else:
        click.echo('Error: no task with id ' + str(fin_taskid))

# Run the app
if __name__ == '__main__':
    todo()
