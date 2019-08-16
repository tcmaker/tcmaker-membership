# frozen_string_literal: true

module ApplicationHelper
  def alert_box(type, message)
    type = type.to_s
    type = 'danger' if type == 'error'
    "<div class=\"alert alert-#{type}\">#{message}</div>".html_safe
  end

  def civicrm_states_dropdown
    usa = CiviCrm::Country.find_by(iso_code: 'US')
    states = CiviCrm::Client.request(:get,
                                     'entity' => 'StateProvince',
                                     'action' => 'get',
                                     'rowCount' => 100,
                                     'country_id' => usa.id)

    ret = []
    states.each do |state|
      ret << [state['name'], state['id']]
    end

    ret
  end

  def format_phone(phone)
    p = Phonelib.parse(phone)
    p.national
  end
end
