import click
from databricks import sql
import os
import json

@click.command()
@click.option('--name', default='World', help='The person to greet.')
def hello(name):


   connection = sql.connect(
                           server_hostname = "adb-4524064152464769.9.azuredatabricks.net",
                           http_path = "/sql/1.0/warehouses/3d58d7311ef7752e",
                           access_token = "dapi35c10a821ebd811a52e94ebdcf47ee4f")

   cursor = connection.cursor()

   cursor.execute("select * from `hive_metastore`.`default`.`fct_dbt__model_executions` WHERE node_id NOT LIKE 'model.dbt_artifacts%' and command_invocation_id='b28f61d7-002d-43b5-985f-1256ae6db83b'")
   rows = cursor.fetchall()

    # Define a list to hold the results
   results = []

    # Iterate through the rows and convert them to dictionaries
   for row in rows:
      result_dict = {}
      for i, column in enumerate(cursor.description):
         result_dict[column[0]] = row[i]
      results.append(result_dict)

   # Print the results as JSON
   print(json.dumps(results, indent=4))

   cursor.close()
   connection.close()
if __name__ == '__main__':
   hello()
