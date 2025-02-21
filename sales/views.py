from django.shortcuts import render
from .forms import SalesSearchForm
from .models import Sale, Book
import pandas as pd
from .utils import get_bookname_from_id, get_chart
from django.contrib.auth.decorators import login_required # to protect function-based views

# Create your views here.
def home(request):
  return render(request, 'sales/home.html')

# define function-based view – records(request)
@login_required # keep protected
def records(request):
  # Handles search for book sales records and displays results
  form = SalesSearchForm(request.POST or None)
  sales_df = None # Initialize dataframe object
  chart = None # Initialize a chart variable

  if request.method == 'POST': # check if the search button is clicked
    book_title = request.POST.get('book_title') # read book_title
    chart_type = request.POST.get('chart_type') # read chart_type

    # Retrieve the book instance from the database (case-insensitive)
    book_instance = Book.objects.filter(name__iexact = book_title).first()

    if book_instance:
      # Retrieve sales records for the selected book
      qs = Sale.objects.filter(book_id = book_instance.id)

      # If sales records exist
      if qs:
        # Convert the QuerySet values to a pandas DataFrame
        sales_df = pd.DataFrame(qs.values())
        # Convert the ID to Name of book
        sales_df['book_id'] = sales_df['book_id'].apply(get_bookname_from_id)

        # Call get_chart by psasing chart_type from user input, sales dataframe and labels
        chart = get_chart(chart_type, sales_df, labels = sales_df['date_created'].values)

        # Convert DataFrame to HTML
        sales_df = sales_df.to_html()

  # Pack up data to be sent to template in the "context" dictionary
  context = {
    'form': form,
    'sales_df': sales_df,
    'chart': chart
  }

  # Load the 'sales/record.html' page using the data that you prepared
  return render(request, 'sales/records.html', context)