module Signup
  class ContactRecordsController < AbstractSignupController
    def new
      @contact_record = ContactRecord.new
    end

    def create
      @contact_record = ContactRecord.new(contact_info_params)
      @contact_record.member_id = session['member_id']
      if @contact_record.save
        progress.update(contact_record_creation_completed: true)
        redirect_to new_signup_membership_path
      else
        render 'new'
      end
    end

    protected

    def contact_info_params
      params.require(:contact_record).permit(
        :street_address,
        :supplemental_address_1,
        :supplemental_address_2,
        :supplemental_address_3,
        :city,
        :state_abbreviation,
        :postal_code,
        :phone,
        :phone_can_receive_sms,
        :emergency_contact_name,
        :emergency_contact_phone)
    end
  end
end
