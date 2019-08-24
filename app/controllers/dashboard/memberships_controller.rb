module Dashboard
  class MembershipsController < AuthenticatedController
    def edit
      @membership = current_member.membership
    end
  end
end
