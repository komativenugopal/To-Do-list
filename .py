class ToDoList:
    def __init__(self):
        self.tasks=[]
    
    def add_task(self,task):
        self.tasks.append(task)
        print(f 'Task "{task}"added successfully.')
    
    def update_task(self,old_task, new_task):
        if task in self.tasks:
            self.tasks.update(task)
            print(f'task "{old_task}" updated to "{new_task}" successfully')
        else:
            print(f'task "{old_task}" not found.')

    def remove_task(self,task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'task "{task} removed successfully')
        else:
            print(f'task "{task}" not found.')
    def view_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for idx, task in enumerate(self.tasks,start=1):
                print(f' {idx}. {task}')
        else:
            print("your To-Do List is empty.")


todo_list = ToDoList()

while True:
    print("\n1. Add Task\n2. Update Task\n3. Remove Task\n4. View Tasks\n5. Exit")
    choice = input("Enter your choice (1/2/3/4):")

    if choice == '1':
        task = input("Enter the task: ")
        todo_list.add_task(task)
    elif choice=='2':
        old_task = input("Enter the task to update: ")
        new_task = input("Enter the new task")
        todo_list.update_task(old_task, new_task,)
    elif choice=='3':
        task=input("Enter the task to remove :")
        todo_list.remove_task(task)
    elif choice=='4':
        todo_list.view_tasks()
        if choice=='5':
            print("Exiting the todo list application")
    else:
        print("invalid choice. please enter 1,2,3,4,5")
