module Signup
  class MembershipsController < AbstractSignupController
    content_security_policy false

    def new
      @membership = Membership.new
    end

    def create
      unless params.key? :stripeToken
        flash[:error] = 'Incorrect credit card entry. Please try again.'
        render 'new'
        return
      end

      unless params.key? :stripeToken
        flash['error'] = 'You must enter payment information'
        render 'new'
        return
      end

      unless ['monthly', 'biannual', 'annual'].include? params['preferred_plan']
        flash['error'] = 'Invalid plan. Try again.'
        render 'new'
        return
      end

      customer = Stripe::Customer.retrieve(current_member.stripe_identifier)
      customer.source = params['stripeToken']
      customer.save

      progress.update!(payment_info_completed: true, preferred_plan: params['preferred_plan'])
      redirect_to new_signup_liability_waiver_path
    end
  end
end
