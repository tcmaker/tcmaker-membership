module Webhooks
  class StripeEventsController < ActionController::API
    def create
      payload = request.body.read
      sig_header = request.headers['HTTP_STRIPE_SIGNATURE']

      binding.pry

      begin
        event = Stripe::Webhook.construct_event(
            payload, sig_header, ENV['STRIPE_WEBHOOK_SIGNING_SECRET']
        )

      rescue JSON::ParserError => e
          # Invalid payload
          status 400
          return

      rescue Stripe::SignatureVerificationError => e
        # Invalid signature
        status 400
        return
      end

      case event.type
      when 'customer.subscription.updated'
        subscription = event.data.object




      end
    end
  end
end
