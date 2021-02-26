from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from datetime import timedelta

Base = declarative_base()


class Table(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

weekday = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}


def menu():
    menu_items = ["\n1) Today's tasks", "2) Week's tasks", "3) All tasks", "4) Missed tasks", "5) Add task", "6) Delete task", "0) Exit"]
    for item in menu_items:
        print(item)


while True:
    today = datetime.today()
    menu()
    selection = input()
    print()
    if selection == '0':  # exit
        print('Bye!')
        break
    elif selection == '1':  # Today
        print('Today ' + str(today.day) + ' ' + today.strftime('%b') + ':')
        today_tasks = session.query(Table).filter(Table.deadline == today.date()).all()
        if len(today_tasks) == 0:
            print("Nothing to do!")
        else:
            i = 1
            for task in today_tasks:
                print(str(i) + '. ' + task.task)
                i += 1
    elif selection == '2':  # Week
        for i in range(7):
            next_day = today + timedelta(days=i)
            print(weekday[next_day.weekday()] + " " + str(next_day.day) + " " + next_day.strftime('%b'))
            day_tasks = session.query(Table).filter(Table.deadline == next_day.date()).all()
            if len(day_tasks) == 0:
                print("Nothing to do!\n")
            else:
                i = 1
                for task in day_tasks:
                    print(str(i) + '. ' + task.task + '\n')
                    i += 1
    elif selection == '3':  # All
        print('All tasks:')
        all_tasks = session.query(Table).order_by(Table.deadline).all()
        if len(all_tasks) == 0:
            print("Nothing to do!\n")
        else:
            i = 1
            for task in all_tasks:
                print(str(i) + '. ' + task.task + ". " + str(task.deadline.day) + " " + task.deadline.strftime('%b'))
                i += 1
    elif selection == '4':  # Missed task
        missed_tasks = session.query(Table).order_by(Table.deadline).filter(Table.deadline < today.date()).all()
        print('Missed tasks:')
        if len(missed_tasks) == 0:
            print('Nothing is missed!')
        else:
            i = 1
            for task in missed_tasks:
                print(str(i) + '. ' + task.task + ". " + str(task.deadline.day) + " " + task.deadline.strftime('%b'))
                i += 1
    elif selection == '5':  # Add task
        new_task = Table(task=input('Enter task\n'), deadline=datetime.strptime(input('Enter deadline\n'), '%Y-%m-%d').date())
        session.add(new_task)
        session.commit()
        print('The task has been added!')
    elif selection == '6':  # Delete task
        print('Choose the number of the task you want to delete:')
        all_tasks = session.query(Table).order_by(Table.deadline).all()
        if len(all_tasks) == 0:
            print("Nothing to delete")
        else:
            i = 1
            for task in all_tasks:
                print(str(i) + '. ' + task.task + ". " + str(task.deadline.day) + " " + task.deadline.strftime('%b'))
                i += 1
            session.delete(all_tasks[int(input()) - 1])
            session.commit()
            print("The task has been deleted!")
