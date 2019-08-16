class AuthenticatedController < ApplicationController
  before_action :authenticate_member!
  before_action :create_breadcrumbs_array
  layout 'authenticated'

  def push_breadcrumb(title, path)
    crumb = OpenStruct.new
    crumb.title = title
    crumb.path = path
    @breadcrumbs << crumb
  end

  def create_breadcrumbs_array
    @breadcrumbs = []
    initialize_breadcrumbs
  end

  # Controllers that subclass AuthenticatedController can override this method,
  # but an empty method needs to exist here as a fallback
  def initialize_breadcrumbs; end
end
