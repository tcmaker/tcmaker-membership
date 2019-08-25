module Dashboard
  class PaymentsController < AuthenticatedController
    content_security_policy false

    def edit
      @current_payment = current_payment_for(current_member)
    end

    def create
      # If validation fails, we'll need to redisplay the edit view.

      unless params['stripe_token'].present?
        @current_payment = current_payment_for(current_member)
        flash['error'] = 'Incorrect card info. Please try again.'
        render 'edit'
      end

      begin
        stripe_customer.source = params['stripe_token']
        stripe_customer.save
        flash[:success] = 'Card Info Updated.'
        redirect_to '/dashboard'
      rescue
        @current_payment = current_payment_for(current_member)
        flash['error'] = 'Incorrect card info. Please try again.'
        render 'edit'
      end
    end

    protected

    def stripe_customer
      @stripe_customer ||= Stripe::Customer.retrieve(current_member.stripe_identifier)
    end

    def current_payment_for(member)
      Stripe::Customer.retrieve_source(
        member.stripe_identifier,
        stripe_customer.default_source
      )
    end
  end
end
