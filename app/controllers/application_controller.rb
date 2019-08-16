class ApplicationController < ActionController::Base
  protected
  helper_method :current_member?
  helper_method :current_member

  def authenticate_member!
    return if session['userinfo']
    session['auth_return_uri'] = request.original_fullpath
    redirect_to oidc_client.authorization_uri(scope: 'openid profile email')
  end

  def current_member?
    session[:userinfo].present?
  end

  def current_member
    @current_member ||= Member.find_by(sub: session['userinfo']['sub'])
  end

  def oidc_client
    @oidc_client ||= OpenIDConnect::Client.new(
      host: ENV['AUTH0_DOMAIN'],
      identifier: ENV['AUTH0_CLIENT_ID'],
      secret: ENV['AUTH0_CLIENT_SECRET'],
      redirect_uri: auth_callback_url,
      authorization_endpoint: "/authorize",
      token_endpoint: "/oauth/token",
      userinfo_endpoint: "/userinfo"
    )
  end
end
