# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AcDetails(models.Model):
    cr_state = models.CharField(max_length=50, blank=True, null=True)
    cr_cons_id = models.IntegerField(blank=True, null=True)
    cons_name = models.CharField(max_length=50, blank=True, null=True)
    cons_type = models.CharField(max_length=50, blank=True, null=True)
    cons_total_voters_count = models.IntegerField(blank=True, null=True)
    cons_male_voters_count = models.IntegerField(blank=True, null=True)
    cons_female_voters_count = models.IntegerField(blank=True, null=True)
    cons_first_male_voter_count = models.IntegerField(blank=True, null=True)
    cons_first_female_voter_count = models.IntegerField(blank=True, null=True)
    cons_poll_perc = models.FloatField(blank=True, null=True)
    cons_third_gender_voter_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_details'
# Unable to inspect table 'ac_mapping'
# The error was: permission denied for table ac_mapping


class AcMappings(models.Model):
    ac_mapping_pk = models.AutoField(primary_key=True)
    state_abb = models.CharField(blank=True, null=True)
    ac_no = models.IntegerField(blank=True, null=True)
    ac_name = models.CharField(blank=True, null=True)
    pc_no = models.IntegerField(blank=True, null=True)
    pc_name = models.CharField(blank=True, null=True)
    district = models.CharField(blank=True, null=True)
    zone = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_mappings'


class ActiveStatesCapi(models.Model):
    state_abb = models.CharField(blank=True, null=True)
    election_cycle = models.CharField(blank=True, null=True)
    election_round = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'active_states_capi'
        unique_together = (('state_abb', 'election_cycle', 'election_round'),)


class AdditionalRemarksCati(models.Model):
    additional_remarks = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField('CatiFact', models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'additional_remarks_cati'


class AddressCati(models.Model):
    address = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField('CatiFact', models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address_cati'


class AeSectionCapi(models.Model):
    capi_fk = models.BigIntegerField(unique=True, blank=True, null=True)
    cand_pref_ques = models.CharField(blank=True, null=True)
    cm_preference = models.CharField(blank=True, null=True)
    cm_work_satisfaction = models.CharField(blank=True, null=True)
    past_vote_pref = models.CharField(blank=True, null=True)
    future_vote_pref = models.CharField(blank=True, null=True)
    mla_work_satisfaction = models.CharField(max_length=50, blank=True, null=True)
    ac_issues = models.CharField(max_length=100, blank=True, null=True)
    ac_winner_preference = models.CharField(max_length=50, blank=True, null=True)
    state_winner_preference = models.CharField(max_length=50, blank=True, null=True)
    state_schemes_benefitted = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ae_section_capi'


class AgeCati(models.Model):
    age = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField('CatiFact', models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'age_cati'




class AgentIdCati(models.Model):
    agent_id = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField('CatiFact', models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_id_cati'


class AgentNameCati(models.Model):
    agent_name = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField('CatiFact', models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_name_cati'


class AlliancePrefQuesCapi(models.Model):
    alliance_pref_ques = models.CharField(blank=True, null=True)
    capi_fk = models.OneToOneField('CapiFact', models.DO_NOTHING, db_column='capi_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alliance_pref_ques_capi'


class AlliancePrefQuesGeCapi(models.Model):
    alliance_pref_ques_ge = models.CharField(blank=True, null=True)
    capi_fk = models.OneToOneField('CapiFact', models.DO_NOTHING, db_column='capi_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alliance_pref_ques_ge_capi'


class AreaSectionCapi(models.Model):
    village = models.CharField(max_length=100, blank=True, null=True)
    nearest_village = models.CharField(max_length=100, blank=True, null=True)
    location_latitude = models.FloatField(blank=True, null=True)
    location_longitude = models.FloatField(blank=True, null=True)
    capi_fk = models.BigIntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area_section_capi'


class AudioUrlCati(models.Model):
    audio_url = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField('CatiFact', models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audio_url_cati'


class AuditSectionCapi(models.Model):
    capi_fk = models.BigIntegerField(primary_key=True)
    audited_datetime = models.CharField(blank=True, null=True)
    remark = models.CharField(blank=True, null=True)
    remark_profiling = models.CharField(blank=True, null=True)
    remark_ae = models.CharField(blank=True, null=True)
    remark_ge = models.CharField(blank=True, null=True)
    collector_unique_id = models.CharField(blank=True, null=True)
    collector_name = models.CharField(blank=True, null=True)
    collector_email = models.CharField(blank=True, null=True)
    auditor_name = models.CharField(blank=True, null=True)
    survey_audio_recordings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit_section_capi'


class BlockCati(models.Model):
    block = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField('CatiFact', models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'block_cati'


class BoothMetadataView(models.Model):
    cons_id = models.IntegerField(blank=True, null=True)
    booth_no = models.IntegerField(blank=True, null=True)
    booth_name_regional = models.CharField(max_length=100, blank=True, null=True)
    main_village_regional = models.CharField(max_length=100, blank=True, null=True)
    panchayat_regional = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    police_station_regional = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    male_voters = models.FloatField(blank=True, null=True)
    female_voters = models.FloatField(blank=True, null=True)
    total_voters = models.FloatField(blank=True, null=True)
    block_regional = models.CharField(max_length=100, blank=True, null=True)
    post_office_regional = models.CharField(max_length=100, blank=True, null=True)
    main_village_eng = models.CharField(max_length=100, blank=True, null=True)
    booth_name_eng = models.CharField(max_length=100, blank=True, null=True)
    booth_address_regional = models.CharField(max_length=100, blank=True, null=True)
    booth_address_eng = models.CharField(max_length=100, blank=True, null=True)
    panchayat_eng = models.CharField(max_length=100, blank=True, null=True)
    block_eng = models.CharField(max_length=100, blank=True, null=True)
    police_station_eng = models.CharField(max_length=100, blank=True, null=True)
    post_office_eng = models.CharField(max_length=100, blank=True, null=True)
    sub_division_eng = models.CharField(max_length=100, blank=True, null=True)
    sub_division_regional = models.CharField(max_length=100, blank=True, null=True)
    cons_name = models.CharField(max_length=50, blank=True, null=True)
    cr_state = models.CharField(max_length=50, blank=True, null=True)
    cr_cons_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booth_metadata_view'


class BoothMetadataViewTest(models.Model):
    cons_id = models.IntegerField(blank=True, null=True)
    booth_no = models.IntegerField(blank=True, null=True)
    booth_name_regional = models.CharField(max_length=100, blank=True, null=True)
    main_village_regional = models.CharField(max_length=100, blank=True, null=True)
    panchayat_regional = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    police_station_regional = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    male_voters = models.IntegerField(blank=True, null=True)
    female_voters = models.IntegerField(blank=True, null=True)
    total_voters = models.FloatField(blank=True, null=True)
    block_regional = models.CharField(max_length=100, blank=True, null=True)
    post_office_regional = models.CharField(max_length=100, blank=True, null=True)
    main_village_eng = models.CharField(max_length=100, blank=True, null=True)
    booth_name_eng = models.CharField(max_length=100, blank=True, null=True)
    booth_address_regional = models.CharField(max_length=100, blank=True, null=True)
    booth_address_eng = models.CharField(max_length=100, blank=True, null=True)
    panchayat_eng = models.CharField(max_length=100, blank=True, null=True)
    block_eng = models.CharField(max_length=100, blank=True, null=True)
    police_station_eng = models.CharField(max_length=100, blank=True, null=True)
    post_office_eng = models.CharField(max_length=100, blank=True, null=True)
    sub_division_eng = models.CharField(max_length=100, blank=True, null=True)
    sub_division_regional = models.CharField(max_length=100, blank=True, null=True)
    cons_name = models.CharField(max_length=50, blank=True, null=True)
    cr_state = models.CharField(max_length=50, blank=True, null=True)
    cr_cons_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booth_metadata_view_test'


class CallRemarkCati(models.Model):
    call_remark = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField('CatiFact', models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'call_remark_cati'


class CandPrefQuesCati(models.Model):
    cand_pref_ques = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField('CatiFact', models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cand_pref_ques_cati'


class CandPrefQuesGeCapi(models.Model):
    cand_pref_ques_ge = models.CharField(blank=True, null=True)
    capi_fk = models.OneToOneField('CapiFact', models.DO_NOTHING, db_column='capi_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cand_pref_ques_ge_capi'


class CapiFact(models.Model):
    capi_pk = models.AutoField(primary_key=True)
    mongo_doc_id = models.CharField(unique=True)
    respondent_unique_id = models.CharField()
    sd_dm_fk = models.ForeignKey('SurveyDescDimensionCapi', models.DO_NOTHING, db_column='sd_dm_fk')
    doc_exists = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'capi_fact'


class CasteCapi(models.Model):
    caste = models.CharField(blank=True, null=True)
    capi_fk = models.OneToOneField(CapiFact, models.DO_NOTHING, db_column='capi_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caste_capi'


class CasteCategoryCati(models.Model):
    caste_category = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField('CatiFact', models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caste_category_cati'


class CasteCati(models.Model):
    caste = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField('CatiFact', models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caste_cati'


class CasteData(models.Model):
    cons_name = models.CharField(max_length=50, blank=True, null=True)
    cr_cons_id = models.IntegerField(blank=True, null=True)
    cd_id = models.IntegerField(blank=True, null=True)
    caste = models.CharField(max_length=50, blank=True, null=True)
    sub_caste = models.CharField(max_length=50, blank=True, null=True)
    caste_perc = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    cr_state = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caste_data'


class CasteOriginalCati(models.Model):
    caste_original = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField('CatiFact', models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caste_original_cati'


class CatiFact(models.Model):
    cati_pk = models.AutoField(primary_key=True)
    mongo_doc_id = models.CharField(unique=True)
    sd_dm_fk = models.ForeignKey('SurveyDescDimensionCati', models.DO_NOTHING, db_column='sd_dm_fk')
    doc_exists = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cati_fact'


class CmWorkSatisfactionCati(models.Model):
    cm_work_satisfaction = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cm_work_satisfaction_cati'


class ConfigsCapi(models.Model):
    state_abb = models.CharField(max_length=50, blank=True, null=True)
    election_cycle = models.CharField(max_length=50, blank=True, null=True)
    election_round = models.CharField(max_length=10, blank=True, null=True)
    main_parties = models.TextField(blank=True, null=True)  # This field type is a guess.
    vn_ae_year = models.IntegerField(blank=True, null=True)
    vn_ge_year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'configs_capi'


class DataUpdatedCati(models.Model):
    data_updated = models.BooleanField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_updated_cati'


class DateCati(models.Model):
    date = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'date_cati'


class DemographicSectionCapi(models.Model):
    capi_fk = models.BigIntegerField(unique=True, blank=True, null=True)
    sub_caste = models.CharField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    age = models.CharField(max_length=10, blank=True, null=True)
    caste_category = models.CharField(max_length=20, blank=True, null=True)
    caste_original = models.CharField(max_length=100, blank=True, null=True)
    sc_sub_caste = models.CharField(max_length=100, blank=True, null=True)
    obc_sub_caste = models.CharField(max_length=100, blank=True, null=True)
    gen_sub_caste = models.CharField(max_length=100, blank=True, null=True)
    st_sub_caste = models.CharField(max_length=100, blank=True, null=True)
    job_type = models.CharField(max_length=100, blank=True, null=True)
    religion = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=30, blank=True, null=True)
    highest_qualification = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demographic_section_capi'


class DesignationCati(models.Model):
    designation = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'designation_cati'


class DistrictCati(models.Model):
    district = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district_cati'


class DrivingFactorToVoteCapi(models.Model):
    driving_factor_to_vote = models.CharField(blank=True, null=True)
    capi_fk = models.OneToOneField(CapiFact, models.DO_NOTHING, db_column='capi_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'driving_factor_to_vote_capi'


class DwSyncTime(models.Model):
    cati = models.DateTimeField(blank=True, null=True)
    capi = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dw_sync_time'


class FarmingIssuesCapi(models.Model):
    farming_issues = models.CharField(blank=True, null=True)
    capi_fk = models.OneToOneField(CapiFact, models.DO_NOTHING, db_column='capi_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farming_issues_capi'


class FinalRejectionCati(models.Model):
    final_rejection = models.BooleanField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'final_rejection_cati'


class Form20DataView(models.Model):
    cons_id = models.IntegerField(blank=True, null=True)
    booth_no_voterroll = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    e_type = models.CharField(max_length=50, blank=True, null=True)
    candidate_name = models.CharField(max_length=100, blank=True, null=True)
    candidate_party = models.CharField(max_length=50, blank=True, null=True)
    votes = models.IntegerField(blank=True, null=True)
    booth_no_form20 = models.CharField(max_length=10, blank=True, null=True)
    cons_name = models.CharField(max_length=50, blank=True, null=True)
    cr_state = models.CharField(max_length=50, blank=True, null=True)
    cr_cons_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form20_data_view'


class FutureVotePrefCati(models.Model):
    future_vote_pref = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'future_vote_pref_cati'


class FutureVotePrefGeCati(models.Model):
    future_vote_pref_ge = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'future_vote_pref_ge_cati'


class GeSectionCapi(models.Model):
    capi_fk = models.BigIntegerField(unique=True, blank=True, null=True)
    cand_pref_ques_ge = models.CharField(max_length=100, blank=True, null=True)
    pm_pref = models.CharField(max_length=100, blank=True, null=True)
    past_vote_pref_ge = models.CharField(max_length=100, blank=True, null=True)
    future_vote_pref_ge = models.CharField(max_length=100, blank=True, null=True)
    pm_work_satisfaction = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ge_section_capi'


class GenderCati(models.Model):
    gender = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gender_cati'


class GramPanchayatCati(models.Model):
    gram_panchayat = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gram_panchayat_cati'


class GramPanchayatEmailCati(models.Model):
    gram_panchayat_email = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gram_panchayat_email_cati'


class GramPanchayatInHindiCati(models.Model):
    gram_panchayat_in_hindi = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gram_panchayat_in_hindi_cati'


class GramPanchayatLgdCodeCati(models.Model):
    gram_panchayat_lgd_code = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gram_panchayat_lgd_code_cati'


class IncumbentGovtSatisfactionCapi(models.Model):
    incumbent_govt_satisfaction = models.CharField(blank=True, null=True)
    capi_fk = models.OneToOneField(CapiFact, models.DO_NOTHING, db_column='capi_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incumbent_govt_satisfaction_capi'


class InterPanchayatCati(models.Model):
    inter_panchayat = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inter_panchayat_cati'


class LastNormalisedCapi(models.Model):
    last_normalised = models.CharField(blank=True, null=True)
    capi_fk = models.OneToOneField(CapiFact, models.DO_NOTHING, db_column='capi_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'last_normalised_capi'


class LscfCapi(models.Model):
    lscf = models.CharField(blank=True, null=True)
    capi_fk = models.OneToOneField(CapiFact, models.DO_NOTHING, db_column='capi_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lscf_capi'


class MarginOfErrorCapi(models.Model):
    sd_dm_fk = models.IntegerField()
    party = models.CharField(max_length=50)
    vn_score = models.CharField(max_length=20)
    moe_value = models.FloatField()
    moe_pk = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'margin_of_error_capi'


class MlaWorkSatisfactionCati(models.Model):
    mla_work_satisfaction = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mla_work_satisfaction_cati'


class MobileCati(models.Model):
    mobile = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mobile_cati'


class MotherTongueCapi(models.Model):
    mother_tongue = models.CharField(blank=True, null=True)
    capi_fk = models.OneToOneField(CapiFact, models.DO_NOTHING, db_column='capi_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mother_tongue_capi'


class NationalSchemeBenefittedCapi(models.Model):
    national_scheme_benefitted = models.CharField(blank=True, null=True)
    capi_fk = models.OneToOneField(CapiFact, models.DO_NOTHING, db_column='capi_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'national_scheme_benefitted_capi'


class NoOfCallingAttemptedCati(models.Model):
    no_of_calling_attempted = models.FloatField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'no_of_calling_attempted_cati'


class NormalisationAcTableCapi(models.Model):
    capi_fk = models.IntegerField(unique=True, blank=True, null=True)
    raw = models.IntegerField(blank=True, null=True)
    vn = models.FloatField(blank=True, null=True)
    vn_final = models.FloatField(blank=True, null=True)
    vn_ae = models.FloatField(blank=True, null=True)
    vn_agc = models.FloatField(blank=True, null=True)
    vn_agc_ae = models.FloatField(blank=True, null=True)
    vn_gc = models.FloatField(blank=True, null=True)
    vn_gc_ae = models.FloatField(blank=True, null=True)
    vn_c = models.FloatField(blank=True, null=True)
    vn_c_ae = models.FloatField(blank=True, null=True)
    vn_ge = models.FloatField(blank=True, null=True)
    vn_ae_ge = models.FloatField(blank=True, null=True)
    vn_raw_ae = models.FloatField(blank=True, null=True)
    vn_average = models.FloatField(blank=True, null=True)
    vn_average_ge = models.FloatField(blank=True, null=True)
    last_normalised_ae = models.BooleanField(blank=True, null=True)
    last_normalised_ge = models.BooleanField(blank=True, null=True)
    caste = models.CharField(max_length=100, blank=True, null=True)
    vn_raw_ge = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'normalisation_ac_table_capi'


class NormalisationDistrictTableCapi(models.Model):
    capi_fk = models.IntegerField(unique=True, blank=True, null=True)
    raw = models.IntegerField(blank=True, null=True)
    vn = models.FloatField(blank=True, null=True)
    vn_final = models.FloatField(blank=True, null=True)
    vn_ae = models.FloatField(blank=True, null=True)
    vn_agc = models.FloatField(blank=True, null=True)
    vn_agc_ae = models.FloatField(blank=True, null=True)
    vn_gc = models.FloatField(blank=True, null=True)
    vn_gc_ae = models.FloatField(blank=True, null=True)
    vn_c = models.FloatField(blank=True, null=True)
    vn_c_ae = models.FloatField(blank=True, null=True)
    vn_ge = models.FloatField(blank=True, null=True)
    vn_ae_ge = models.FloatField(blank=True, null=True)
    vn_raw_ae = models.FloatField(blank=True, null=True)
    vn_average = models.FloatField(blank=True, null=True)
    vn_average_ge = models.FloatField(blank=True, null=True)
    last_normalised_ae = models.BooleanField(blank=True, null=True)
    last_normalised_ge = models.BooleanField(blank=True, null=True)
    caste = models.CharField(max_length=100, blank=True, null=True)
    vn_raw_ge = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'normalisation_district_table_capi'


class NormalisationPcTableCapi(models.Model):
    capi_fk = models.IntegerField(unique=True, blank=True, null=True)
    raw = models.IntegerField(blank=True, null=True)
    vn = models.FloatField(blank=True, null=True)
    vn_final = models.FloatField(blank=True, null=True)
    vn_ae = models.FloatField(blank=True, null=True)
    vn_agc = models.FloatField(blank=True, null=True)
    vn_agc_ae = models.FloatField(blank=True, null=True)
    vn_gc = models.FloatField(blank=True, null=True)
    vn_gc_ae = models.FloatField(blank=True, null=True)
    vn_c = models.FloatField(blank=True, null=True)
    vn_c_ae = models.FloatField(blank=True, null=True)
    vn_ge = models.FloatField(blank=True, null=True)
    vn_ae_ge = models.FloatField(blank=True, null=True)
    vn_raw_ae = models.FloatField(blank=True, null=True)
    vn_average = models.FloatField(blank=True, null=True)
    vn_average_ge = models.FloatField(blank=True, null=True)
    last_normalised_ae = models.BooleanField(blank=True, null=True)
    last_normalised_ge = models.BooleanField(blank=True, null=True)
    caste = models.CharField(max_length=100, blank=True, null=True)
    vn_raw_ge = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'normalisation_pc_table_capi'


class NormalisationStateTableCapi(models.Model):
    capi_fk = models.IntegerField(unique=True, blank=True, null=True)
    raw = models.IntegerField(blank=True, null=True)
    vn = models.FloatField(blank=True, null=True)
    vn_final = models.FloatField(blank=True, null=True)
    vn_ae = models.FloatField(blank=True, null=True)
    vn_agc = models.FloatField(blank=True, null=True)
    vn_agc_ae = models.FloatField(blank=True, null=True)
    vn_gc = models.FloatField(blank=True, null=True)
    vn_gc_ae = models.FloatField(blank=True, null=True)
    vn_c = models.FloatField(blank=True, null=True)
    vn_c_ae = models.FloatField(blank=True, null=True)
    vn_ge = models.FloatField(blank=True, null=True)
    vn_ae_ge = models.FloatField(blank=True, null=True)
    vn_raw_ae = models.FloatField(blank=True, null=True)
    vn_average = models.FloatField(blank=True, null=True)
    vn_average_ge = models.FloatField(blank=True, null=True)
    last_normalised_ae = models.BooleanField(blank=True, null=True)
    last_normalised_ge = models.BooleanField(blank=True, null=True)
    caste = models.CharField(max_length=100, blank=True, null=True)
    vn_raw_ge = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'normalisation_state_table_capi'


class NormalisationTableCapi(models.Model):
    capi_fk = models.IntegerField(unique=True, blank=True, null=True)
    raw = models.IntegerField(blank=True, null=True)
    vn = models.FloatField(blank=True, null=True)
    vn_final = models.FloatField(blank=True, null=True)
    vn_ae = models.FloatField(blank=True, null=True)
    vn_agc = models.FloatField(blank=True, null=True)
    vn_agc_ae = models.FloatField(blank=True, null=True)
    vn_gc = models.FloatField(blank=True, null=True)
    vn_gc_ae = models.FloatField(blank=True, null=True)
    vn_c = models.FloatField(blank=True, null=True)
    vn_c_ae = models.FloatField(blank=True, null=True)
    vn_ge = models.FloatField(blank=True, null=True)
    vn_ae_ge = models.FloatField(blank=True, null=True)
    vn_raw_ae = models.FloatField(blank=True, null=True)
    vn_average = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'normalisation_table_capi'


class NormalisationTableCati(models.Model):
    cati_fk = models.IntegerField(unique=True, blank=True, null=True)
    raw = models.IntegerField(blank=True, null=True)
    vn = models.FloatField(blank=True, null=True)
    vn_final = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'normalisation_table_cati'


class NormalisationZoneTableCapi(models.Model):
    capi_fk = models.IntegerField(unique=True, blank=True, null=True)
    raw = models.IntegerField(blank=True, null=True)
    vn = models.FloatField(blank=True, null=True)
    vn_final = models.FloatField(blank=True, null=True)
    vn_ae = models.FloatField(blank=True, null=True)
    vn_agc = models.FloatField(blank=True, null=True)
    vn_agc_ae = models.FloatField(blank=True, null=True)
    vn_gc = models.FloatField(blank=True, null=True)
    vn_gc_ae = models.FloatField(blank=True, null=True)
    vn_c = models.FloatField(blank=True, null=True)
    vn_c_ae = models.FloatField(blank=True, null=True)
    vn_ge = models.FloatField(blank=True, null=True)
    vn_ae_ge = models.FloatField(blank=True, null=True)
    vn_raw_ae = models.FloatField(blank=True, null=True)
    vn_average = models.FloatField(blank=True, null=True)
    vn_average_ge = models.FloatField(blank=True, null=True)
    last_normalised_ae = models.BooleanField(blank=True, null=True)
    last_normalised_ge = models.BooleanField(blank=True, null=True)
    caste = models.CharField(max_length=100, blank=True, null=True)
    vn_raw_ge = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'normalisation_zone_table_capi'


class OtherQuesCapi(models.Model):
    capi_fk = models.BigIntegerField()
    ques_mapping_fk = models.BigIntegerField()
    ans = models.TextField(blank=True, null=True)
    alliance_pref = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_ques_capi'
        unique_together = (('capi_fk', 'ques_mapping_fk'),)


class OtherQuesCati(models.Model):
    cati_fk = models.ForeignKey(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)
    ques = models.CharField(max_length=300)
    ans = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_ques_cati'
        unique_together = (('ques', 'cati_fk'),)


class OtherQuesMappingCapi(models.Model):
    otm_pk = models.AutoField(primary_key=True)
    ques = models.CharField(unique=True, max_length=500)

    class Meta:
        managed = False
        db_table = 'other_ques_mapping_capi'


class PastVotePrefGeCapi(models.Model):
    past_vote_pref_ge = models.CharField(blank=True, null=True)
    capi_fk = models.OneToOneField(CapiFact, models.DO_NOTHING, db_column='capi_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'past_vote_pref_ge_capi'
# Unable to inspect table 'qc_checks_fvp'
# The error was: permission denied for table qc_checks_fvp


class ReasonToVoteCapi(models.Model):
    reason_to_vote = models.CharField(blank=True, null=True)
    capi_fk = models.OneToOneField(CapiFact, models.DO_NOTHING, db_column='capi_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reason_to_vote_capi'


class ReligionCati(models.Model):
    religion = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'religion_cati'


class RetroAllianceMapping(models.Model):
    retro_alliance_mapping_pk = models.BigAutoField(primary_key=True)
    state_abb = models.CharField(max_length=3)
    el_year = models.SmallIntegerField()
    e_type = models.CharField(max_length=10)
    party = models.CharField(max_length=100)
    alliance = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'retro_alliance_mapping'
        unique_together = (('state_abb', 'el_year', 'e_type', 'party', 'alliance'),)
        db_table_comment = 'Table contains state wise alliance and political parties that were part of the alliance state and year wise.'


class RetroDataMaterialised(models.Model):
    org_state = models.CharField(max_length=50, blank=True, null=True)
    el_year = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    e_type = models.CharField(max_length=50, blank=True, null=True)
    cr_cons_id = models.IntegerField(blank=True, null=True)
    cons_name = models.CharField(max_length=50, blank=True, null=True)
    ca_full_name = models.CharField(max_length=100, blank=True, null=True)
    ca_id = models.IntegerField(blank=True, null=True)
    org_abb = models.CharField(max_length=50, blank=True, null=True)
    el_vote_count = models.BigIntegerField(blank=True, null=True)
    el_vote_perc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    el_rank = models.IntegerField(blank=True, null=True)
    e_id = models.IntegerField(blank=True, null=True)
    op_pos_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'retro_data_materialised'


class SeatCallCapi(models.Model):
    sd_dm_fk = models.IntegerField()
    vn_score = models.CharField(max_length=30)
    seat_call = models.CharField(max_length=100)
    seat_call_pk = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'seat_call_capi'
        unique_together = (('sd_dm_fk', 'vn_score'),)
# Unable to inspect table 'special_tn_ac_mappings'
# The error was: permission denied for table special_tn_ac_mappings


class SubCasteCati(models.Model):
    sub_caste = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_caste_cati'


class SurveyAllianceMapping(models.Model):
    survey_alliance_mapping_pk = models.BigAutoField(primary_key=True)
    election_cycle = models.CharField(max_length=20)
    election_round = models.CharField(max_length=10)
    party = models.CharField(max_length=100)
    alliance = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'survey_alliance_mapping'
        unique_together = (('election_cycle', 'election_round', 'party', 'alliance'),)
        db_table_comment = 'Table contains state wise alliance and political parties that are part of the tentative alliance, state and year wise.'


class SurveyDescDimensionCapi(models.Model):
    sd_dm_pk = models.AutoField(primary_key=True)
    state_abb = models.CharField(blank=True, null=True)
    election_cycle = models.CharField()
    election_round = models.CharField()
    level = models.CharField()
    cons_no = models.IntegerField()
    status = models.CharField()
    reporting_round = models.CharField()
    ac_mapping_fk = models.ForeignKey(AcMappings, models.DO_NOTHING, db_column='ac_mapping_fk', blank=True, null=True)
    audit_status = models.CharField()
    normalisation = models.CharField()
    recalibration_status = models.CharField()

    class Meta:
        managed = False
        db_table = 'survey_desc_dimension_capi'
        unique_together = (('state_abb', 'election_cycle', 'election_round', 'level', 'cons_no'),)


class SurveyDescDimensionCati(models.Model):
    sd_dm_pk = models.AutoField(primary_key=True)
    state_abb = models.CharField(blank=True, null=True)
    election_cycle = models.CharField()
    election_round = models.CharField()
    cons_no = models.IntegerField()
    campaign_id = models.CharField()

    class Meta:
        managed = False
        db_table = 'survey_desc_dimension_cati'
        unique_together = (('state_abb', 'election_cycle', 'election_round', 'cons_no'),)


class SyncDateCati(models.Model):
    sync_date = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sync_date_cati'


class SyncTimeCati(models.Model):
    sync_time = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sync_time_cati'


class TalkDurationCati(models.Model):
    talk_duration = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'talk_duration_cati'


class TeamCodeCapi(models.Model):
    team_code = models.CharField(blank=True, null=True)
    capi_fk = models.OneToOneField(CapiFact, models.DO_NOTHING, db_column='capi_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_code_capi'


class TimeCati(models.Model):
    time = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_cati'


class TimeSectionCapi(models.Model):
    end_date = models.CharField(max_length=20, blank=True, null=True)
    end_time = models.CharField(max_length=20, blank=True, null=True)
    sync_date = models.CharField(max_length=20, blank=True, null=True)
    sync_time = models.CharField(max_length=20, blank=True, null=True)
    start_date = models.CharField(max_length=20, blank=True, null=True)
    time_duration = models.FloatField(blank=True, null=True)
    capi_fk = models.BigIntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_section_capi'


class TimeValidationCati(models.Model):
    time_validation = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_validation_cati'


class TimeValidationFlagCati(models.Model):
    time_validation_flag = models.BooleanField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_validation_flag_cati'


class TotalDurationCati(models.Model):
    total_duration = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'total_duration_cati'


class V1RejectionCati(models.Model):
    v1_rejection = models.BooleanField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v1_rejection_cati'


class V1RejectionSectionCapi(models.Model):
    mandatory_ques_rejection = models.BooleanField(blank=True, null=True)
    future_vote_pref_rejection = models.BooleanField(blank=True, null=True)
    mobile_number_rejection = models.BooleanField(blank=True, null=True)
    lat_long_rejection = models.BooleanField(blank=True, null=True)
    v1_rejection = models.BooleanField(blank=True, null=True)
    capi_fk = models.BigIntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v1_rejection_section_capi'


class V1ValidationSectionCapi(models.Model):
    mobile_validation = models.BooleanField(blank=True, null=True)
    past_vote_validation = models.BooleanField(blank=True, null=True)
    third_party_validation = models.BooleanField(blank=True, null=True)
    time_validation = models.BooleanField(blank=True, null=True)
    v1_validation = models.BooleanField(blank=True, null=True)
    religion_validation = models.BooleanField(blank=True, null=True)
    capi_fk = models.BigIntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v1_validation_section_capi'


class V2RejectionCati(models.Model):
    v2_rejection = models.BooleanField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v2_rejection_cati'


class VillageCati(models.Model):
    village = models.CharField(blank=True, null=True)
    cati_fk = models.OneToOneField(CatiFact, models.DO_NOTHING, db_column='cati_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'village_cati'


class VillageSamplingCapi(models.Model):
    pk = models.CompositePrimaryKey('election_cycle', 'election_round', 'ac_no', 'village_name_eng')
    election_cycle = models.CharField(max_length=10)
    election_round = models.CharField(max_length=10)
    ac_no = models.SmallIntegerField()
    village_name_eng = models.CharField(max_length=200)
    village_name_regional = models.CharField(max_length=200, blank=True, null=True)
    samples_to_collect = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'village_sampling_capi'
