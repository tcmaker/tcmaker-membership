class DoorService
  def self.activate(keyfob)
    msg = JSON.generate({
      keyfob: keyfob,
      action: 'activate'
    })
    sqs_client.send_message(queue_url: queue_url, message_body: msg)
  end

  def self.deactivate(keyfob)
    msg = JSON.generate({
      keyfob: keyfob,
      action: 'deactivate'
    })
    sqs_client.send_message(queue_url: queue_url, message_body: msg)
  end

  def self.sqs_client
    Aws::SQS::Client.new(region: ENV['AWS_REGION'])
  end

  def self.queue_url
    queues = sqs_client.list_queues
    queues.queue_urls.first
  end
end
