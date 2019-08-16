class AuthController < ApplicationController
  def callback
    oidc_client.authorization_code = params['code']
    tokens = oidc_client.access_token!(scope: 'openid profile email')

    access_token = tokens.access_token
    id_token = tokens.id_token
    decoded_id_token = Auth0Service.decode_jwt(id_token)
    userinfo = tokens.userinfo!
    session['userinfo'] = userinfo
    redirect_to session['auth_return_uri']

  end

  def logout
    reset_session
    redirect_to logout_url.to_s
  end

  protected

  def logout_url
    domain = ENV['AUTH0_DOMAIN']
    client_id = ENV['AUTH0_CLIENT_ID']
    request_params = {
      returnTo: 'https://tcmaker.org/',
      client_id: client_id
    }

    URI::HTTPS.build(host: domain, path: '/v2/logout', query: to_query(request_params))
  end

  def to_query(hash)
    hash.map { |k, v| "#{k}=#{URI.escape(v)}" unless v.nil? }.reject(&:nil?).join('&')
  end
end
