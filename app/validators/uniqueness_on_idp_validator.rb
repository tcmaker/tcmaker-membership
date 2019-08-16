class UniquenessOnIdpValidator < ActiveModel::EachValidator
  def validate_each(record, attribute, value)
    users = api.users({
      q: build_lucene_query(attribute, value),
      per_page: 1,
      search_engine: 'v3' })
    return if users.empty?
    return if users.first['user_id'] == record.sub
    record.errors.add(attribute, "The #{attribute} you supplied is already in use")
  end

  protected

  def api
    @api ||= Auth0Service.api_client
  end

  # This is ugly, but separating out the query string makes it easier for me to
  # tweak search options
  def build_lucene_query(attribute, value)
    terms = [
      [attribute.to_s, '"%s"' % value].join(':'),
      ["identities.connection", '"%s"' % ENV['AUTH0_CONNECTION_NAME']].join(':')
    ].join(' AND ')
    terms
  end
end
