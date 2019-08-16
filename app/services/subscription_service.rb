class SubscriptionService
  def self.handle_subscription_update(subscription)
    case subscription.status
    when 'incomplete', 'incomplete_expired', 'past_due', 'canceled', 'unpaid'
      # deactivate keyfob
    when 'active'
      # activate keyfob
    end
  end
end
