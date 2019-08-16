module Dashboard
  class ContactRecordsController < AuthenticatedController
    def edit
      @contact_record = current_member.contact_record
      push_breadcrumb('Change Contact Information', edit_dashboard_contact_record_path)
    end

    def update
      @contact_record = ContactRecord.find(current_member.contact_record)

      if @contact_record.update(contact_record_params)
        redirect_to '/dashboard'
      else
        render 'edit'
      end
    end

    def contact_record_params
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
