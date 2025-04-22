import { TodoList } from './todo.js';
const todo = new TodoList();
todo.addTask("Learn ES6 Modules");
todo.addTask("Build a Todo App");
todo.completeTask(0);
todo.listTasks();