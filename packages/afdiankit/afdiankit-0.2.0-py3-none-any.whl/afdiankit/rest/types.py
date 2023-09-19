"""DO NOT EDIT THIS FILE!

This file is automatically @generated by afdiankit using the follow command:

    python -m codegen && isort . && black .
"""

from __future__ import annotations

from typing import TypedDict


class PostLogCollectRequestBody(TypedDict):
    stat_id: str
    uri: str
    refer: str


class PostVerifyCodeRequestBody(TypedDict):
    account: str
    password: str
    name: str


class PostRegRequestBody(TypedDict):
    account: str
    password: str
    name: str
    code: str
    mp_token: str


class PostLoginRequestBody(TypedDict):
    account: str
    password: str
    mp_token: str


class PostQuickLoginRequestBody(TypedDict):
    account: str
    code: str
    mp_token: str


class PostSendQlCodeRequestBody(TypedDict):
    account: str


class PostQuickLoginCodeRequestBody(TypedDict):
    account: str


class PostSendForgetCodeRequestBody(TypedDict):
    account: str


class PostCheckForgetCodeRequestBody(TypedDict):
    account: str
    code: str


class PostResetPasswordRequestBody(TypedDict):
    token: str
    password: str


class PostEditBasicRequestBody(TypedDict):
    name: str
    avatar: str
    url_slug: str
    category_id: str
    type: str
    doing: str
    detail: str
    pic: str
    cover: str
    watermark: str


class PostEditPlanRequestBody(TypedDict):
    plan_id: str
    name: str
    price: str
    desc: str
    pic: str
    status: str
    reply_switch: str
    reply_content: str
    reply_random_switch: str
    reply_random_content: str
    independent: str
    permanent: str
    sku: list
    need_address: str
    pay_month: str
    favorable_price: str
    product_discount_price: str
    product_vip_price: str
    vip_price_related_plan_ids: str
    has_time_limit_price: int
    time_limit_begin: str
    time_limit_end: str
    time_limit_price: str
    time_limit_discount: str
    product_type: str
    bundle_stock: str
    bundle_sku_select_count: str
    product_vip_price_include_history: int
    has_plan_config: int
    remark_name: str
    remark_placeholder: str
    remark_required: str
    can_ali_agreement: str


class PostDelPlanRequestBody(TypedDict):
    plan_id: str


class PostEditWithdrawRequestBody(TypedDict):
    realname: str
    account: str
    type: str


class GetOrderPrepareRequestBody(TypedDict):
    plan_id: str
    user_id: str
    sku_detail: str
    product_type: str


class PostCreateOrderRequestBody(TypedDict):
    plan_id: str
    month: str
    total_amount: str
    out_trade_no: str
    pay_type: str
    code: str
    user_id: str
    per_month: str
    remark: str
    mp_token: str
    show_amount: str
    addr_name: str
    addr_phone: str
    addr_address: str
    sku_detail: list
    plan_invite_code: str
    custom_order_id: str
    cmid: str
    card_id_list: list
    ticket_round_id: str
    agreement: str


class GetOrderCancelRequestBody(TypedDict):
    out_trade_no: str


class GetMyApplyWithdrawRequestBody(TypedDict):
    ...


class PostMyEditBasicRequestBody(TypedDict):
    avatar: str
    name: str
    addr_name: str
    addr_phone: str
    addr_address: str
    gender: str
    birthday: str


class PostMessageSendRequestBody(TypedDict):
    user_id: str
    type: str
    content: str


class PostPostPublishRequestBody(TypedDict):
    post_id: str
    vote_id: str
    cate: str
    title: str
    content: str
    pics: str
    is_public: str
    min_price: str
    audio: str
    video: str
    audio_thumb: str
    video_thumb: str
    type: int
    cover: str
    group_id: str
    is_feed: int
    plan_ids: str
    album_ids: str
    attachment: list
    timing: str
    optype: str
    preview_text: str


class PostPostDeleteRequestBody(TypedDict):
    post_id: str


class PostCreatorRemAlbumPostRequestBody(TypedDict):
    post_id: str
    album_id: str


class PostPostLikeRequestBody(TypedDict):
    post_id: str


class PostPostUnlikeRequestBody(TypedDict):
    post_id: str


class PostCommentLikeRequestBody(TypedDict):
    comment_id: str


class PostCommentUnlikeRequestBody(TypedDict):
    comment_id: str


class PostCreatorCustomPlanSwitchRequestBody(TypedDict):
    status: str
    desc: str


class PostCreatorHidePlanRequestBody(TypedDict):
    plan_id: str


class PostCreatorShowPlanRequestBody(TypedDict):
    plan_id: str


class PostCommentPublishRequestBody(TypedDict):
    post_id: str
    content: str
    reply_comment_id: str


class PostCreatorEditThankWordRequestBody(TypedDict):
    content: str
    month: str
    year: str
    pic: str


class PostEditGoalRequestBody(TypedDict):
    goal_id: str
    monthly_fans: str
    monthly_income: str
    desc: str
    type: int
    status: int
    begin_time: str
    end_time: str


class PostDelGoalRequestBody(TypedDict):
    goal_id: str


class PostCreatorHideGoalRequestBody(TypedDict):
    goal_id: str


class PostCreatorShowGoalRequestBody(TypedDict):
    goal_id: str


class PostAccountSendVerifyCodeRequestBody(TypedDict):
    account: str


class PostAccountChangePasswordRequestBody(TypedDict):
    old_password: str
    new_password: str


class PostAccountBindRequestBody(TypedDict):
    account: str
    code: str


class PostMyCreatorSharePageRequestBody(TypedDict):
    ...


class PostOauthMpRedirectUriRequestBody(TypedDict):
    redirect_uri: str


class PostOauthMpCodeRequestBody(TypedDict):
    code: str


class PostOauthMxRedirectUriRequestBody(TypedDict):
    redirect_uri: str


class PostOauthMxCodeRequestBody(TypedDict):
    code: str


class PostCreatorDiscountOptionRequestBody(TypedDict):
    status: str


class PostCommentDeleteRequestBody(TypedDict):
    comment_id: str


class PostCreatorShowGuideRequestBody(TypedDict):
    status: str


class PostCreatorPrivacyPublicIncomeRequestBody(TypedDict):
    status: str


class PostCreatorPrivacyPublicSponsorRequestBody(TypedDict):
    status: str


class PostTopRequestBody(TypedDict):
    post_id: str


class PostUntopRequestBody(TypedDict):
    post_id: str


class PostCreatorEditAlbumRequestBody(TypedDict):
    album_id: str
    title: str
    content: str
    cover: str


class PostCreatorEditAlbumPostRequestBody(TypedDict):
    album_id: str
    post_ids: str


class PostCreatorUpdateAlbumPostOrderByRequestBody(TypedDict):
    album_id: str
    order_by: str


class GetCreatorDelAlbumRequestBody(TypedDict):
    album_id: str


class PostCreatorShowAlbumRequestBody(TypedDict):
    status: str


class PostCreatorShowShopRequestBody(TypedDict):
    status: str


class PostCreatorSetShowSponsorRequestBody(TypedDict):
    status: str


class GetCreatorEditGroupRequestBody(TypedDict):
    group_id: str
    title: str
    content: str
    cover: str
    type: str
    price: str
    join_group_type: str
    selected_plan: str


class GetUserJoinGroupRequestBody(TypedDict):
    group_id: str


class PostCreatorOpenGroupSwitchRequestBody(TypedDict):
    group_id: str
    status: str


class PostPostTopGroupRequestBody(TypedDict):
    post_id: str


class PostPostUntopGroupRequestBody(TypedDict):
    post_id: str


class PostUploadGetSignRequestBody(TypedDict):
    type: str


class PostUploadGetUrlRequestBody(TypedDict):
    url: str
    type: str


class PostCreatorMakeRedeemRequestBody(TypedDict):
    plan_id: str
    num: str
    sku_id: str


class PostUserUseRedeemRequestBody(TypedDict):
    redeem_id: str
    addr_name: str
    addr_phone: str
    addr_address: str


class PostSetCanBuyHideRequestBody(TypedDict):
    plan_id: str
    status: str


class PostUserMarkRequestBody(TypedDict):
    user_id: str


class PostUserUnmarkRequestBody(TypedDict):
    user_id: str


class PostUserQuitGroupRequestBody(TypedDict):
    group_id: str


class PostCreatorSubmitCertificationRequestBody(TypedDict):
    url: str


class PostCreatorCopyTextRequestBody(TypedDict):
    status: str


class PostCreatorCopyPicRequestBody(TypedDict):
    status: str


class PostApiUserBlackRequestBody(TypedDict):
    user_id: str
    type: str


class PostApiUserUnblackRequestBody(TypedDict):
    user_id: str
    type: str


class PostUserShowSponsoringRequestBody(TypedDict):
    status: str


class PostApiFaqAskRequestBody(TypedDict):
    id: str
    user_id: str


class PostApiFaqAnswerRequestBody(TypedDict):
    id: str
    user_id: str


class PostOrderUpdateExpressRequestBody(TypedDict):
    out_trade_no: str
    company_id: str
    express_no: str


class PostOrderUpdateAddressRequestBody(TypedDict):
    out_trade_no: str
    addr_name: str
    addr_phone: str
    addr_address: str


class PostMyWhoSponsoredMeRequestBody(TypedDict):
    page: int
    sort_field: str
    sort_value: str
    filter: list
    per_page: int


class PostMyCheckSendMsgBatchRequestBody(TypedDict):
    filter: list
    is_all: int
    include_user_ids: list
    exclude_user_ids: list
    type: str
    content: str


class PostMySendMsgBatchRequestBody(TypedDict):
    filter: list
    is_all: int
    include_user_ids: list
    exclude_user_ids: list
    type: str
    content: str


class PostCreatorCreateOpenTokenRequestBody(TypedDict):
    ...


class PostCreatorUpdateOpenWebhookRequestBody(TypedDict):
    url: str


class PostCreatorTestOpenWebhookRequestBody(TypedDict):
    url: str


class PostEditVoteRequestBody(TypedDict):
    vote_id: str
    chosen_type: str
    chosen_max: str
    title: str
    deadline: int
    options: list
    deadline_type: str


class PostCastVoteRequestBody(TypedDict):
    vote_id: str
    vote: list


class PostMessageCreateWorkOrderRequestBody(TypedDict):
    msg_id: str
    type: str


class GetOauthJssdkSignRequestBody(TypedDict):
    url: str


class PostUserMarkPostRequestBody(TypedDict):
    post_id: str


class PostUserUnmarkPostRequestBody(TypedDict):
    post_id: str


class PostUpdateUserFeedSettingRequestBody(TypedDict):
    sponsoring: str
    unlock: str
    in_blacklist: str
    user_id: str


class PostGoalSettingSponsorRequestBody(TypedDict):
    status: str


class PostGoalSettingProductRequestBody(TypedDict):
    status: str


class PostMyUpdateNotifyRequestBody(TypedDict):
    status: str
    field: str


class PostShowProductCountSetRequestBody(TypedDict):
    count: str


class PostApiCreatorSearchRequestBody(TypedDict):
    user_id: str
    keyword: str
    type: str
    page: int


class PostBangCusApplicationRequestBody(TypedDict):
    copy: str
    national: str
    number: str
    name: str
    valid_time: str
    mobile_number: str
    bank_acct_no: str
    bank_code: str
    bank_branch_code: str
    sms_code: str


class PostBangCusApplicationRenewRequestBody(TypedDict):
    copy: str
    national: str
    number: str
    name: str
    valid_time: str
    mobile_number: str
    bank_acct_no: str
    bank_code: str
    bank_branch_code: str
    sms_code: str


class PostSuiyinziSetPersonMemberRequestBody(TypedDict):
    mobile: str
    identity_no: str
    identity_front_img_no: str
    identity_back_img_no: str
    identity_no_valid_date: str
    account_name: str
    account_no: str
    bank_code: str


class PostChangeDefaultWithdrawMethodRequestBody(TypedDict):
    withdraw_type: str


class PostEditCreatorBadgeRequestBody(TypedDict):
    images: str
    badge_id: str
    selected_plan: str


class PostBadgeGetUserBadgeDetailRequestBody(TypedDict):
    badge_set_id: str
    user_id: str


class PostSetShowBadgeRequestBody(TypedDict):
    display_status: str
    badge_set_id: str


class PostOrderUpdateCreatorRemarkRequestBody(TypedDict):
    out_trade_no: str
    creator_remark: str


class PostOauth2ClientInfoRequestBody(TypedDict):
    client_id: str


class PostOauth2AuthorizeRequestBody(TypedDict):
    response_type: str
    client_id: str
    redirect_uri: str
    state: str
    scope: str


class PostEditPlanRankRequestBody(TypedDict):
    plan_ids: str


class PostUserIdcardValidateRequestBody(TypedDict):
    id_card: str
    name: str
    phone: str
    license_type: str
    is_self: str


class PostUserEditIdcardRequestBody(TypedDict):
    id_card: str
    name: str
    phone: str
    license_type: str
    id: str


class PostReportRequestBody(TypedDict):
    object_type: str
    object_id: str
    report_type: str
    report_reason: str


class PostAccountSubmitCancellationRequestBody(TypedDict):
    account: str
    password: str
    reason: str
    content: str


class PostAccountCancelCancellationRequestBody(TypedDict):
    ...


class PostDeleteSponsorRelationRequestBody(TypedDict):
    remote_id: str


class PostAddTeamMemberRequestBody(TypedDict):
    account: str
    member_name: str


class PostDeleteTeamMemberRequestBody(TypedDict):
    user_id: str


class PostEditTeamMemberRequestBody(TypedDict):
    user_id: str
    member_name: str


__all__ = [
    "PostLogCollectRequestBody",
    "PostVerifyCodeRequestBody",
    "PostRegRequestBody",
    "PostLoginRequestBody",
    "PostQuickLoginRequestBody",
    "PostSendQlCodeRequestBody",
    "PostQuickLoginCodeRequestBody",
    "PostSendForgetCodeRequestBody",
    "PostCheckForgetCodeRequestBody",
    "PostResetPasswordRequestBody",
    "PostEditBasicRequestBody",
    "PostEditPlanRequestBody",
    "PostDelPlanRequestBody",
    "PostEditWithdrawRequestBody",
    "GetOrderPrepareRequestBody",
    "PostCreateOrderRequestBody",
    "GetOrderCancelRequestBody",
    "GetMyApplyWithdrawRequestBody",
    "PostMyEditBasicRequestBody",
    "PostMessageSendRequestBody",
    "PostPostPublishRequestBody",
    "PostPostDeleteRequestBody",
    "PostCreatorRemAlbumPostRequestBody",
    "PostPostLikeRequestBody",
    "PostPostUnlikeRequestBody",
    "PostCommentLikeRequestBody",
    "PostCommentUnlikeRequestBody",
    "PostCreatorCustomPlanSwitchRequestBody",
    "PostCreatorHidePlanRequestBody",
    "PostCreatorShowPlanRequestBody",
    "PostCommentPublishRequestBody",
    "PostCreatorEditThankWordRequestBody",
    "PostEditGoalRequestBody",
    "PostDelGoalRequestBody",
    "PostCreatorHideGoalRequestBody",
    "PostCreatorShowGoalRequestBody",
    "PostAccountSendVerifyCodeRequestBody",
    "PostAccountChangePasswordRequestBody",
    "PostAccountBindRequestBody",
    "PostMyCreatorSharePageRequestBody",
    "PostOauthMpRedirectUriRequestBody",
    "PostOauthMpCodeRequestBody",
    "PostOauthMxRedirectUriRequestBody",
    "PostOauthMxCodeRequestBody",
    "PostCreatorDiscountOptionRequestBody",
    "PostCommentDeleteRequestBody",
    "PostCreatorShowGuideRequestBody",
    "PostCreatorPrivacyPublicIncomeRequestBody",
    "PostCreatorPrivacyPublicSponsorRequestBody",
    "PostTopRequestBody",
    "PostUntopRequestBody",
    "PostCreatorEditAlbumRequestBody",
    "PostCreatorEditAlbumPostRequestBody",
    "PostCreatorUpdateAlbumPostOrderByRequestBody",
    "GetCreatorDelAlbumRequestBody",
    "PostCreatorShowAlbumRequestBody",
    "PostCreatorShowShopRequestBody",
    "PostCreatorSetShowSponsorRequestBody",
    "GetCreatorEditGroupRequestBody",
    "GetUserJoinGroupRequestBody",
    "PostCreatorOpenGroupSwitchRequestBody",
    "PostPostTopGroupRequestBody",
    "PostPostUntopGroupRequestBody",
    "PostUploadGetSignRequestBody",
    "PostUploadGetUrlRequestBody",
    "PostCreatorMakeRedeemRequestBody",
    "PostUserUseRedeemRequestBody",
    "PostSetCanBuyHideRequestBody",
    "PostUserMarkRequestBody",
    "PostUserUnmarkRequestBody",
    "PostUserQuitGroupRequestBody",
    "PostCreatorSubmitCertificationRequestBody",
    "PostCreatorCopyTextRequestBody",
    "PostCreatorCopyPicRequestBody",
    "PostApiUserBlackRequestBody",
    "PostApiUserUnblackRequestBody",
    "PostUserShowSponsoringRequestBody",
    "PostApiFaqAskRequestBody",
    "PostApiFaqAnswerRequestBody",
    "PostOrderUpdateExpressRequestBody",
    "PostOrderUpdateAddressRequestBody",
    "PostMyWhoSponsoredMeRequestBody",
    "PostMyCheckSendMsgBatchRequestBody",
    "PostMySendMsgBatchRequestBody",
    "PostCreatorCreateOpenTokenRequestBody",
    "PostCreatorUpdateOpenWebhookRequestBody",
    "PostCreatorTestOpenWebhookRequestBody",
    "PostEditVoteRequestBody",
    "PostCastVoteRequestBody",
    "PostMessageCreateWorkOrderRequestBody",
    "GetOauthJssdkSignRequestBody",
    "PostUserMarkPostRequestBody",
    "PostUserUnmarkPostRequestBody",
    "PostUpdateUserFeedSettingRequestBody",
    "PostGoalSettingSponsorRequestBody",
    "PostGoalSettingProductRequestBody",
    "PostMyUpdateNotifyRequestBody",
    "PostShowProductCountSetRequestBody",
    "PostApiCreatorSearchRequestBody",
    "PostBangCusApplicationRequestBody",
    "PostBangCusApplicationRenewRequestBody",
    "PostSuiyinziSetPersonMemberRequestBody",
    "PostChangeDefaultWithdrawMethodRequestBody",
    "PostEditCreatorBadgeRequestBody",
    "PostBadgeGetUserBadgeDetailRequestBody",
    "PostSetShowBadgeRequestBody",
    "PostOrderUpdateCreatorRemarkRequestBody",
    "PostOauth2ClientInfoRequestBody",
    "PostOauth2AuthorizeRequestBody",
    "PostEditPlanRankRequestBody",
    "PostUserIdcardValidateRequestBody",
    "PostUserEditIdcardRequestBody",
    "PostReportRequestBody",
    "PostAccountSubmitCancellationRequestBody",
    "PostAccountCancelCancellationRequestBody",
    "PostDeleteSponsorRelationRequestBody",
    "PostAddTeamMemberRequestBody",
    "PostDeleteTeamMemberRequestBody",
    "PostEditTeamMemberRequestBody",
]
