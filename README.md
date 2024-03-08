Welcome to my Employee Management project—a journey into understanding the intricacies of database operations in Django. Let me guide you through this simple yet powerful application with some captivating visuals.

<span style="font-size:28px;">Get ready to enhance your team by effortlessly adding new employees!</span>

![Employee Add Section](assets/employee_add_sec.png)

By simply clicking the "Add Employee" button, you unlock the gateway to expanding your workforce. The process is intuitive, and the application seamlessly guides you through every step.

Once you've added an employee, get ready for the magic! You'll be whisked away to the dynamic realm of the Employee List—a digital database showcasing the heart and soul of your team.

![Employee List Section](assets/employee_list_sec.png)

Marvel at the organized collection of team members, each represented with vital details. This visual representation offers a quick overview and makes managing your team a breeze.

Feeling intrigued? Eager to dive in and experience it for yourself? Here's a step-by-step tutorial on how you can run this application on your system:


## Usage Instructions
Clone this repository e.g.

```bash
$ https://github.com/sumankarki9/Django-Employee-Management.git
```

after you cloned repo, go to the cloned repo directory and run the following command

```bash

cd Django-Employee-Management  #Moving into the project folder


$ pip install Django # Install Django

$ python manage.py makemigrations
```
This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```bash  
$ python manage.py migrate
```

That was pretty simple, right? Now let's make the App live. We just need to start the server now and then we can start using our simple Employee Management App. Start the server by following command

```bash

$ python manage.py runserver
```
Once the server is hosted, head over to http://127.0.0.1:8000 for the App.
