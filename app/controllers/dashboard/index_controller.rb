module Dashboard
  class IndexController < AuthenticatedController
    def index
      customer = Stripe::Customer.retrieve(current_member.stripe_identifier)
      @subscription = customer.subscriptions.first
    end
  end
end
