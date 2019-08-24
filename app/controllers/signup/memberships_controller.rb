module Signup
  class MembershipsController < AbstractSignupController
    content_security_policy false

    def new
      @preferred_plan = 'monthly'
    end

    def create
      @preferred_plan = params['preferred_plan']

      unless params.key? :stripeToken
        flash[:error] = 'Incorrect credit card entry. Please try again.'
        render 'new'
        return
      end

      unless ['monthly', 'biannual', 'annual'].include? params['preferred_plan']
        flash['error'] = 'Invalid plan. Try again.'
        render 'new'
        return
      end

      begin
        customer = Stripe::Customer.retrieve(current_member.stripe_identifier)
        customer.source = params['stripeToken']
        customer.save
      rescue
        flash[:error] = 'Incorrect credit card entry. Please try again.'
      end

      progress.update!(payment_info_completed: true, preferred_plan: params['preferred_plan'])
      redirect_to new_signup_liability_waiver_path
    end
  end
end
