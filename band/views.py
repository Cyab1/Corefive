from django.shortcuts import render, redirect
from .models import Member, Event, Ticket
from django.contrib.auth.decorators import login_required
from django.db import DatabaseError
from django.http import HttpResponse
from django.db import transaction


@login_required
@login_required
def events(request):
    try:
        events = Event.objects.all()
        return render(request, "events.html", {"events": events})
    except DatabaseError as e:
        print(f"Database error: {e}")
        return HttpResponse(
            "An error occurred while fetching events. Please try again later."
        )


def home(request):
    try:
        return render(request, "home.html")
    except Exception as e:
        print(f"Rendering error: {e}")
        return HttpResponse(
            "An error occurred while loading the home page. Please try again later."
        )


def members(request):
    try:
        members = Member.objects.all()
        return render(request, "members.html", {"members": members})
    except DatabaseError as e:
        print(f"Database error: {e}")
        return HttpResponse(
            "An error occurred while fetching members. Please try again later."
        )


@login_required
def purchase_ticket(request):
    try:
        events = Event.objects.all()
    except Exception as e:
        print(f"Error fetching events: {e}")
        return HttpResponse(
            "An error occurred while fetching events. Please try again later."
        )

    if request.method == "POST":
        try:
            with transaction.atomic():
                event_id = int(request.POST.get("event"))
                quantity = int(request.POST.get("quantity", 1))

                event = Event.objects.get(id=event_id)
                total_cost = quantity * event.price

                # Create a new ticket
                ticket = Ticket.objects.create(
                    user=request.user,
                    event=event,
                    quantity=quantity,
                    total_cost=total_cost,
                )

                # Redirect to a success page
                return render(
                    request,
                    "purchase_success.html",
                    {
                        "ticket": ticket,
                        "event": event,
                        "quantity": quantity,
                        "total_cost": total_cost,
                    },
                )

        except (ValueError, TypeError, Event.DoesNotExist) as e:
            print(f"Error processing ticket purchase: {e}")
            return render(
                request,
                "purchase_error.html",
                {
                    "error_message": "An error occurred while processing your purchase. Please try again."
                },
            )

    # If it's a GET request, we'll use events from the database
    return render(request, "purchase_ticket.html", {"events": events})
