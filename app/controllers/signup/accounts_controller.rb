module Signup
  class AccountsController < AbstractSignupController
    def new
      @member = Member.new
    end

    def create
      @member = Member.create(member_params)
      if @member.persisted?
        session['member_id'] = @member.id
        Progress.create!(member: @member, account_creation_completed: true)
        redirect_to new_signup_contact_record_path
      else
        render 'new'
      end
    end

    protected

    def member_params
      params.require(:member).permit(:first_name, :last_name, :email, :username, :password, :password_confirmation)
    end
  end
end
