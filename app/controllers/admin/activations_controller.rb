module Admin
  class ActivationsController < AuthenticatedController
    def index
      @activations = []
      Signup::Progress.pending_activation.find_each do |record|
        @activations << Activation.new({
          id: record.id,
          name: record.member.name,
          member_id: record.member_id,
          plan: record.preferred_plan
        })
      end
    end

    def show
      progress = Signup::Progress.find(params[:id])
      @activation = Activation.new(
        id: progress.id,
        name: progress.member.name,
        member_id: progress.member_id,
        plan: progress.preferred_plan
      )
    end

    def edit
      progress = Signup::Progress.find(params[:id])
      @activation = Activation.new(
        id: progress.id,
        name: progress.member.name,
        member_id: progress.member_id,
        plan: progress.preferred_plan
      )
      @select_options = [
        ['Monthly Membership', 'monthly'],
        ['Six-Month Membership', 'biannual'],
        ['Twelve-Month Membership', 'annual']
      ]
    end

    def update
      @activation = Activation.new(activation_params)
      progress = Signup::Progress.find(params['id'])
      plans = Stripe::Plan.list.map {|i| [i.nickname, i.id]}.to_h
      stripe_api_payload = {
        customer: progress.member.stripe_identifier,
        items: [
          {
            plan: plans[@activation.plan],
          },
        ],
      }
      result = Stripe::Subscription.create(stripe_api_payload)

      progress.update!(membership_activation_completed: true)
      progress.member.update!(keyfob_code: @activation.keyfob_code)

      flash[:success] = 'Member successfully activated.'
      redirect_to admin_activations_path
    end

    protected

    def activation_params
      params.require(:admin_activation).permit(:plan, :keyfob_code)
    end
  end
end
