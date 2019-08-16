# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 2019_08_20_014920) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "capabilities", force: :cascade do |t|
    t.string "name"
    t.string "short_name"
    t.text "description"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "contact_records", force: :cascade do |t|
    t.bigint "member_id"
    t.string "street_address"
    t.string "supplemental_address_1"
    t.string "supplemental_address_2"
    t.string "supplemental_address_3"
    t.string "city"
    t.string "state_abbreviation"
    t.string "postal_code"
    t.string "phone"
    t.boolean "phone_can_receive_sms", default: false, null: false
    t.string "emergency_contact_name"
    t.string "emergency_contact_phone"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["member_id"], name: "index_contact_records_on_member_id"
  end

  create_table "endorsements", force: :cascade do |t|
    t.bigint "member_id"
    t.bigint "capability_id"
    t.bigint "granted_by_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["capability_id"], name: "index_endorsements_on_capability_id"
    t.index ["granted_by_id"], name: "index_endorsements_on_granted_by_id"
    t.index ["member_id"], name: "index_endorsements_on_member_id"
  end

  create_table "members", force: :cascade do |t|
    t.string "sub", null: false
    t.string "first_name", null: false
    t.string "last_name", null: false
    t.string "username", null: false
    t.string "email", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string "stripe_identifier"
    t.string "crm_identifier"
    t.string "keyfob_code"
    t.boolean "accepted_liability_waiver"
  end

  create_table "signup_progresses", force: :cascade do |t|
    t.bigint "member_id"
    t.boolean "account_creation_completed", default: false, null: false
    t.boolean "contact_record_creation_completed", default: false, null: false
    t.boolean "payment_info_completed", default: false, null: false
    t.boolean "liability_waiver_completed", default: false, null: false
    t.boolean "membership_activation_completed", default: false, null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string "preferred_plan"
    t.index ["member_id"], name: "index_signup_progresses_on_member_id"
  end

end
