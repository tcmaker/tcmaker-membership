module Signup
  class IndexController < AbstractSignupController
    def index
      redirect_to new_signup_account_path
    end

    def done
      reset_session
    end
  end
end
