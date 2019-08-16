# frozen_string_literal: true

class Auth0Service

  def self.create_user!(member)
    api = api_client
    result = api.create_user(member.name, {
      username: member.username,
      given_name: member.first_name,
      family_name: member.last_name,
      email: member.email,
      password: member.password,
      connection: ENV['AUTH0_CONNECTION_NAME']
    })
    member['sub'] = result['user_id']
    member
  end

  def self.get_access_token
    url = URI("https://#{ENV['AUTH0_DOMAIN']}/oauth/token")
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    http.verify_mode = OpenSSL::SSL::VERIFY_NONE

    request = Net::HTTP::Post.new(url)
    request['content-type'] = 'application/json'
    request.body = JSON.dump(
      grant_type: 'client_credentials',
      client_id: ENV['AUTH0_MAINTENANCE_CLIENT_ID'],
      client_secret: ENV['AUTH0_MAINTENANCE_CLIENT_SECRET'],
      audience: "https://#{ENV['AUTH0_DOMAIN']}/api/v2/"
    )

    response = http.request(request)
    unless response.is_a? Net::HTTPSuccess
      puts response.read_body
      response.error!
    end

    JSON.parse(response.read_body)
  end

  def self.api_client
    Auth0Client.new(
      client_id: ENV['AUTH0_MAINTENANCE_CLIENT_ID'],
      token: get_access_token['access_token'],
      domain: ENV['AUTH0_DOMAIN'],
      api_version: 2,
      timeout: 15 # optional, defaults to 10
    )
  end

  # See: https://auth0.com/docs/quickstart/backend/rails/01-authorization
  def self.decode_jwt(token)
    JWT.decode(token, nil,
               true, # Verify the signature of this token
               algorithm: 'RS256',
               iss: "https://#{ENV['AUTH0_DOMAIN']}/",
               verify_iss: true,
               aud: Rails.application.secrets.auth0_api_audience,
               verify_aud: true) do |header|
      jwks_hash[header['kid']]
    end
  end

  def self.jwks_hash
    jwks_raw = Net::HTTP.get URI("https://#{ENV['AUTH0_DOMAIN']}/.well-known/jwks.json")
    jwks_keys = Array(JSON.parse(jwks_raw)['keys'])
    Hash[
      jwks_keys
      .map do |k|
        [
          k['kid'],
          OpenSSL::X509::Certificate.new(
            Base64.decode64(k['x5c'].first)
          ).public_key
        ]
      end
    ]
  end
end
