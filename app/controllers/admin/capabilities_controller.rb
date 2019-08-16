module Admin
  class CapabilitiesController < AuthenticatedController
    def index
      @capabilities = Capability.all
    end

    def new
      @capability = Capability.new
    end

    def create
    end

    protected
  end
end
