from books.models import Book # You need to connect parameters from books model
from io import BytesIO
import base64
import matplotlib.pyplot as plt

# Define a function that takes the ID
def get_bookname_from_id(val):
  # This ID is used to retrieve the name from the record
  bookname = Book.objects.get(id = val)
  # And the name is returned back
  return bookname

def get_graph():
  # Create a BytesIO buffer for the image
  buffer = BytesIO()

  # Create a plot with a bytesIO object as a file-like object. Set format to png
  plt.savefig(buffer, format = 'png')

  # Set cursor to the beginning of the stream
  buffer.seek(0)

  # Retrieve the content of the file
  image_png = buffer.getvalue()

  # Encode the bytes-like object
  graph = base64.b64encode(image_png)

  # Decode to get the string as output
  graph = graph.decode('utf-8')

  # Free up the memory of buffer
  buffer.close()

  # Return the image/graph
  return graph

# chart-type: user input o type of chart,
# data: pandas dataframe
def get_chart(chart_type, data, **kwargs):
  # Switch plot backend to AGG (Anti-Grain Geometry) – to write to file
  # AGG is preferred solution to write PNG files
  plt.switch_backend('AGG')

  # Specify figure size
  fig = plt.figure(figsize = (6, 3))

  # Select chart_type based on user input from the form
  if chart_type == '#1':
    # Plot bar chart between date on x-axis and quantity on y-axis
    plt.bar(data['date_created'], data['quantity'])

  elif chart_type == '#2':
    # Generate pie chart based on the price
    # The book titles are sent from the view as labels
    labels = kwargs.get('labels')
    plt.pie(data['price'], labels = labels)

  elif chart_type == '#3':
    # Plot line chart based on date on x-axis and price on y-axis
    plt.plot(data['date_created'], data['price'])

  else:
    print('Unknown chart type')
  
  # Specify layout details
  plt.tight_layout()

  # Render the graph to file
  chart = get_graph()
  return chart