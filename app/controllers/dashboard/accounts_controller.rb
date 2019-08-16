module Dashboard
  class AccountsController < AuthenticatedController
    before_action :find_member
    def edit
      push_breadcrumb('Change Basic Information', edit_dashboard_account_path)
    end

    def update
      if @member.update(account_params)
        redirect_to '/dashboard'
      else
        render 'edit'
      end
    end

    protected

    def account_params
      params.require(:member).permit(:first_name, :last_name, :email)
    end

    def find_member
      @member = Member.find(current_member.id)
    end
  end
end
