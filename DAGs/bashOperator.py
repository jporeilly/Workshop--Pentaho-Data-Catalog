# Example DAG to test bashOperator

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

# Define default_args and other DAG parameters
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 4, 2),
    'retries': 1,
}

# Create the DAG
with DAG('my_bash_script_dag', default_args=default_args, schedule_interval=None) as dag:
    # Define a task that executes a bash command
    run_script_task = BashOperator(
        task_id='run_my_script',
        bash_command='echo "Hello, Airflow!"',
    )

# Add any other tasks or dependencies as needed
# ...

# Set up the execution order of tasks
run_script_task  # This task will execute the bash command
# Add other tasks here if needed
