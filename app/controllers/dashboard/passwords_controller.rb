# frozen_string_literal: true

module Dashboard
  class PasswordsController < AuthenticatedController
    def edit
      @password = Password.new
      push_breadcrumb('Change Password', edit_dashboard_password_path)
    end

    def update
      @password = Password.new(password_params)
      if @password.validate
        begin
          Auth0Service.api_client.patch_user(current_member.sub,
                                             password: @password.password)
          flash[:success] = 'Password updated.'
          redirect_to '/dashboard'
        rescue StandardError
          flash[:error] = 'Your password sucks. Try again.'
          render 'edit'
        end
      else
        render 'edit'
      end
    end

    protected

    def password_params
      params.require(:dashboard_password).permit(:password, :password_confirmation)
    end
  end
end
