

class ToDoList:
    
    task_list = []

    def task_add(self, task:str):
        self.task_list.append(task)
    
    def task_remove(self, index:int):
        self.task_list.remove(index)
    
    def print_task(self, index:int):
        print("#" + index + " " + self.task_list(index))
            
    def print_task_all(self):
        count = self.task_list.count
        x = 1

        while x < count: 
            print("#" + x + " " + self.task_list(x))