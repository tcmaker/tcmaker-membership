module Signup
  class AbstractSignupController < ApplicationController
    layout 'signup'

    def current_member
      @current_member ||= Member.find(session[:member_id])
    end

    def progress
      @progress ||= Progress.find_by(member_id: session[:member_id])
    end
  end
end
