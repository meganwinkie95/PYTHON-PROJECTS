from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction

# THis function will render the home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None) #Retrieve Transaction form
    # Checks if request method is POST
    if request.method == 'POST':
        pk = request.POST['account'] # If the form is submitted, retrieve which account the user wants to view
        return balance(request, pk) # call balance function to render that account's Balance Sheet
    content = {'form': form} #pass content to the template in a dictionary
    # Adds content of form to page
    return render(request, 'checkbook/index.html', content)


# This function will render the create new account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None)
    #Checks if request method is POST
    if request.method == 'POST':
        if form.is_valid(): #Check to see if the submitted form is valid and if so, saves the form
            form.save()
            return redirect('index') #Returns user back tot he home page
    content = {'form': form} #Saves content to the template as a directory
    #adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)


def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)
    transactions = Transaction.Transactions.filter(account=pk)
    current_total = account.initial_deposit
    table_contents = {}
    for t in transactions:
        if t.type == 'Deposit':
            current_total += t.amount
            table_contents.update({t: current_total})
        else:
            current_total -= t.amount
            table_contents.update({t: current_total})

    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


def transaction(request):
    form = TransactionForm(data=request.POST or None)
    # Checks if request method is POST
    if request.method == 'POST':
        if form.is_valid(): # Check to see if the submitted form is valid and if so, saves the form
            pk = request.POST['account']
            form.save()
            return balance(request, pk)
            return redirect('index')  # Returns user back to the home page
    content = {'form': form}  # Saves content to the template as a directory
    # adds content of form to page
    return render(request, 'checkbook/AddTransaction.html', content)