from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import UserDbForm
from .models import OrderItem, Order, BillingAddress, ShopMain, Shirts, Shorts, Watches, Pants, Shoes, item, Slippers, \
    TopProductOne, TopProduct, LatestProduct, LatestProductOne, ReviewProductOne, ReviewProduct, PostForm, Post
from .forms import CreateUserForm, CheckoutForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import DetailView, ListView, View
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def Signup(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "SignUp successful")

    context = {'form': form}
    return render(request, 'accounts/Signup.html', context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_page')

        else:
            messages.info(request, "Email or Password is incorrect")

    context = {}
    return render(request, 'accounts/login.html', context)


def posts_list(request):
    query = None
    results = []
    if request.method == "GET":
        query = request.GET.get('search')
        results = ShopMain.objects.filter(Q(title__icontains=query) | Q(image__icontains=query))
    return render(request, 'customer.html', {'query': query, 'results': results})


def logoutuser(request):
    logout(request)
    return redirect('login')


def home(request):
    items_one = LatestProduct.objects.all()
    items_two = ReviewProduct.objects.all()
    items_three = TopProduct.objects.all()
    items_four = LatestProductOne.objects.all()
    items_five = ReviewProductOne.objects.all()
    items_six = TopProductOne.objects.all()
    context = {
        'items_one': items_one,
        'items_two': items_two,
        'items_three': items_three,
        'items_four': items_four,
        'items_five': items_five,
        'items_six': items_six
    }
    return render(request, 'base.html', context)


class shop(ListView):
    model = ShopMain
    paginate_by = 12
    template_name = "shop-grid.html"


def blg(request):
    return render(request, 'blog.html')


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }
        return render(self.request, 'checkout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                First_name = form.cleaned_data.get('First_name')
                Last_name = form.cleaned_data.get('Last_name')
                Email = form.cleaned_data.get('Email')
                Country = form.cleaned_data.get('Country')
                street_address = form.cleaned_data.get('street_address')
                Apartment_address = form.cleaned_data.get('Apartment_address')
                Town_or_City = form.cleaned_data.get('Town_or_City')
                Zip = form.cleaned_data.get('Zip')
                Phone = form.cleaned_data.get('Phone')
                #same_billing_address = form.cleaned_data.get('same_billing_address')
                #save_info = form.cleaned_data.get('save_info')
                #payment_option = form.cleaned_data.get('payment_option')
                #save_as_birthday = form.cleaned_data.get('save_as_birthday')

                billing_address = BillingAddress(
                    user=self.request.user,
                    First_name=First_name,
                    Last_name=Last_name,
                    Email=Email,
                    Country=Country,
                    street_address=street_address,
                    Apartment_address=Apartment_address,
                    Town_or_City=Town_or_City,
                    Zip=Zip,
                    Phone=Phone
                )
                billing_address.save()
                order.billing_address = billing_address
                order.save()

                return redirect('checkout')
        except ObjectDoesNotExist:
            return redirect("order_summary")

        return redirect('checkout')


class PaymentView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'payment.html')


def contact(request):
    form = UserDbForm()
    if request.method == "POST":
        form = UserDbForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'contact.html', context)


class ShopListView(ListView):
    model = Shoes
    paginate_by = 9
    template_name = 'Shoes.html'


class ShopDetailsView(DetailView):
    model = ShopMain
    template_name = "shop-details.html"


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Shoes, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated")

        else:
            messages.info(request, "This item was added to your cart")
            order.items.add(order_item)

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item quantity was updated")
    return redirect("shop-details", slug=slug)


@login_required
def add_item_to_cart(request, slug):
    item = get_object_or_404(Shoes, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()

        else:
            order.items.add(order_item)

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect("order_summary")


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Shoes, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your cart")
            return redirect("shop-details", slug=slug)

        else:
            messages.info(request, "This item was not in your cart")
            return redirect("shop-details", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
    return redirect("shop-details", slug=slug)


@login_required
def remove_total_from_cart(request, slug):
    item = get_object_or_404(Shoes, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            order.items.remove(order_item)
            return redirect("order_summary")

        else:
            return redirect("order_summary")
    else:
        return redirect("order_summary")


@login_required
def remove_single_from_cart(request, slug):
    item = get_object_or_404(Shoes, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
            else:
                order.items.remove(order_item)
            order_item.save()
            return redirect("order_summary")

        else:
            return redirect("order_summary")
    else:
        return redirect("order_summary")


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'shoping-cart.html', context)

        except ObjectDoesNotExist:
            return redirect("/")


def blg_details(request):
    return render(request, 'blog-details.html')


def index(request):
    return render(request, 'index.html')


class SlippersListView(ListView):
    model = Slippers
    paginate_by = 9
    template_name = 'Slippers.html'


class ShortsListView(ListView):
    model = Shorts
    paginate_by = 9
    template_name = 'Shorts.html'


class WatchesListView(ListView):
    model = Watches
    paginate_by = 9
    template_name = 'Watches.html'


class ShirtsListView(ListView):
    model = Shirts
    paginate_by = 9
    template_name = 'Shirts.html'


class PantsListView(ListView):
    model = Pants
    paginate_by = 9
    template_name = 'Pants.html'


class PostView(ListView):
    model = Post
    template_name = 'posts.html'


class Posts(DetailView):
    model = PostForm
    template_name = 'postforms.html'


def answers(request):
    context = {}
    return render(request, 'answers.html', context)







