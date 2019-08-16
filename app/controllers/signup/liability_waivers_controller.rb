module Signup
  class LiabilityWaiversController < AbstractSignupController
    def new
      @waiver = LiabilityWaiver.new
    end

    def create
      @waiver = LiabilityWaiver.new(liability_waiver_params)

      if @waiver.validate
        progress.update!(liability_waiver_completed: true)
        current_member.update(accepted_liability_waiver: true)

        redirect_to '/signup/done'
      else
        render 'new'
      end
    end

    protected

    def liability_waiver_params
      params.require(:liability_waiver).permit(:waives_liability)
    end
  end
end
