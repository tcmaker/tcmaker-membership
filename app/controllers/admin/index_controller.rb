module Admin
  class IndexController < AuthenticatedController
    def index
      @activations = Signup::Progress.pending_activation.all
    end
  end
end
