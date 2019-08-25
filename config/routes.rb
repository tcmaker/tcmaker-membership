Rails.application.routes.draw do
  # Misc routes
  root to: 'index#index'
  get 'auth/signin' => 'auth#signin'
  get 'auth/callback' => 'auth#callback'
  get 'auth/failure' => 'auth#failure'
  get 'auth/logout' => 'auth#logout'
  get 'legal/liability_waiver' => 'legal#liability_waiver'

  namespace :admin do
    root to: 'index#index'
    resources :members
    resources :capabilities
    resources :permits
    resources :notifications
    resources :memberships
    resources :activations, only: [:index, :show, :edit, :update]
  end

  namespace :api do
    namespace :v0 do
      resources :user_events
    end
  end

  namespace :dashboard do
    root to: 'index#index'

    resource :account
    resource :contact_record
    resource :membership
    resource :payment
    resource :password
  end

  namespace :signup do
    root to: 'index#index'
    get 'done' => 'index#done'

    resource :account
    resource :contact_record
    resource :membership
    resource :liability_waiver
  end

  namespace :webhooks do
    resources :stripe_events, only: [:create]
  end
end
