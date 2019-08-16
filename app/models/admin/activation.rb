module Admin
  class Activation
    include ActiveModel:: Model

    attr_accessor :id
    attr_accessor :name
    attr_accessor :member_id
    attr_accessor :plan
    attr_accessor :keyfob_code

    def member
      Member.find(member_id)
    end
  end
end
