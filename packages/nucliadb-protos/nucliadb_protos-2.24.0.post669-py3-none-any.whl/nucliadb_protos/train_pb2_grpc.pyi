"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import collections.abc
import grpc
import nucliadb_protos.train_pb2
import nucliadb_protos.writer_pb2
from nucliadb_protos.knowledgebox_pb2 import (
    CONFLICT as CONFLICT,
    CleanedKnowledgeBoxResponse as CleanedKnowledgeBoxResponse,
    DeleteKnowledgeBoxResponse as DeleteKnowledgeBoxResponse,
    DeletedEntitiesGroups as DeletedEntitiesGroups,
    ERROR as ERROR,
    EntitiesGroup as EntitiesGroup,
    EntitiesGroupSummary as EntitiesGroupSummary,
    EntitiesGroups as EntitiesGroups,
    Entity as Entity,
    GCKnowledgeBoxResponse as GCKnowledgeBoxResponse,
    KnowledgeBox as KnowledgeBox,
    KnowledgeBoxConfig as KnowledgeBoxConfig,
    KnowledgeBoxID as KnowledgeBoxID,
    KnowledgeBoxNew as KnowledgeBoxNew,
    KnowledgeBoxPrefix as KnowledgeBoxPrefix,
    KnowledgeBoxResponseStatus as KnowledgeBoxResponseStatus,
    KnowledgeBoxUpdate as KnowledgeBoxUpdate,
    Label as Label,
    LabelSet as LabelSet,
    Labels as Labels,
    NOTFOUND as NOTFOUND,
    NewKnowledgeBoxResponse as NewKnowledgeBoxResponse,
    OK as OK,
    SemanticModelMetadata as SemanticModelMetadata,
    Synonyms as Synonyms,
    TermSynonyms as TermSynonyms,
    UpdateKnowledgeBoxResponse as UpdateKnowledgeBoxResponse,
    VectorSet as VectorSet,
    VectorSets as VectorSets,
)
from nucliadb_protos.resources_pb2 import (
    AllFieldIDs as AllFieldIDs,
    Basic as Basic,
    Block as Block,
    CONVERSATION as CONVERSATION,
    Classification as Classification,
    CloudFile as CloudFile,
    ComputedMetadata as ComputedMetadata,
    Conversation as Conversation,
    DATETIME as DATETIME,
    Entity as Entity,
    Extra as Extra,
    ExtractedTextWrapper as ExtractedTextWrapper,
    ExtractedVectorsWrapper as ExtractedVectorsWrapper,
    FILE as FILE,
    FieldClassifications as FieldClassifications,
    FieldComputedMetadata as FieldComputedMetadata,
    FieldComputedMetadataWrapper as FieldComputedMetadataWrapper,
    FieldConversation as FieldConversation,
    FieldDatetime as FieldDatetime,
    FieldFile as FieldFile,
    FieldID as FieldID,
    FieldKeywordset as FieldKeywordset,
    FieldLargeMetadata as FieldLargeMetadata,
    FieldLayout as FieldLayout,
    FieldLink as FieldLink,
    FieldMetadata as FieldMetadata,
    FieldText as FieldText,
    FieldType as FieldType,
    FileExtractedData as FileExtractedData,
    FilePages as FilePages,
    GENERIC as GENERIC,
    KEYWORDSET as KEYWORDSET,
    Keyword as Keyword,
    LAYOUT as LAYOUT,
    LINK as LINK,
    LargeComputedMetadata as LargeComputedMetadata,
    LargeComputedMetadataWrapper as LargeComputedMetadataWrapper,
    LayoutContent as LayoutContent,
    LinkExtractedData as LinkExtractedData,
    Message as Message,
    MessageContent as MessageContent,
    Metadata as Metadata,
    NestedListPosition as NestedListPosition,
    NestedPosition as NestedPosition,
    Origin as Origin,
    PagePositions as PagePositions,
    PageSelections as PageSelections,
    PageStructure as PageStructure,
    PageStructurePage as PageStructurePage,
    PageStructureToken as PageStructureToken,
    Paragraph as Paragraph,
    ParagraphAnnotation as ParagraphAnnotation,
    Position as Position,
    Positions as Positions,
    Relations as Relations,
    RowsPreview as RowsPreview,
    Sentence as Sentence,
    TEXT as TEXT,
    TokenSplit as TokenSplit,
    UserFieldMetadata as UserFieldMetadata,
    UserMetadata as UserMetadata,
    UserVectorsWrapper as UserVectorsWrapper,
    VisualSelection as VisualSelection,
)
from nucliadb_protos.writer_pb2 import (
    Audit as Audit,
    BinaryData as BinaryData,
    BinaryMetadata as BinaryMetadata,
    BrokerMessage as BrokerMessage,
    DelEntitiesRequest as DelEntitiesRequest,
    DelLabelsRequest as DelLabelsRequest,
    DelVectorSetRequest as DelVectorSetRequest,
    Error as Error,
    ExportRequest as ExportRequest,
    FileRequest as FileRequest,
    FileUploaded as FileUploaded,
    GetEntitiesGroupRequest as GetEntitiesGroupRequest,
    GetEntitiesGroupResponse as GetEntitiesGroupResponse,
    GetEntitiesRequest as GetEntitiesRequest,
    GetEntitiesResponse as GetEntitiesResponse,
    GetLabelSetRequest as GetLabelSetRequest,
    GetLabelSetResponse as GetLabelSetResponse,
    GetLabelsRequest as GetLabelsRequest,
    GetLabelsResponse as GetLabelsResponse,
    GetSynonymsResponse as GetSynonymsResponse,
    GetVectorSetsRequest as GetVectorSetsRequest,
    GetVectorSetsResponse as GetVectorSetsResponse,
    IndexResource as IndexResource,
    IndexStatus as IndexStatus,
    ListEntitiesGroupsRequest as ListEntitiesGroupsRequest,
    ListEntitiesGroupsResponse as ListEntitiesGroupsResponse,
    ListMembersRequest as ListMembersRequest,
    ListMembersResponse as ListMembersResponse,
    Member as Member,
    MergeEntitiesRequest as MergeEntitiesRequest,
    NewEntitiesGroupRequest as NewEntitiesGroupRequest,
    NewEntitiesGroupResponse as NewEntitiesGroupResponse,
    Notification as Notification,
    OpStatusWriter as OpStatusWriter,
    ResourceFieldExistsResponse as ResourceFieldExistsResponse,
    ResourceFieldId as ResourceFieldId,
    ResourceIdRequest as ResourceIdRequest,
    ResourceIdResponse as ResourceIdResponse,
    SetEntitiesRequest as SetEntitiesRequest,
    SetLabelsRequest as SetLabelsRequest,
    SetSynonymsRequest as SetSynonymsRequest,
    SetVectorSetRequest as SetVectorSetRequest,
    SetVectorsRequest as SetVectorsRequest,
    SetVectorsResponse as SetVectorsResponse,
    ShardObject as ShardObject,
    ShardReplica as ShardReplica,
    Shards as Shards,
    SynonymsRequest as SynonymsRequest,
    UpdateEntitiesGroupRequest as UpdateEntitiesGroupRequest,
    UpdateEntitiesGroupResponse as UpdateEntitiesGroupResponse,
    UploadBinaryData as UploadBinaryData,
    WriterStatusRequest as WriterStatusRequest,
    WriterStatusResponse as WriterStatusResponse,
)

class TrainStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    GetInfo: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.train_pb2.GetInfoRequest,
        nucliadb_protos.train_pb2.TrainInfo,
    ]
    GetSentences: grpc.UnaryStreamMultiCallable[
        nucliadb_protos.train_pb2.GetSentencesRequest,
        nucliadb_protos.train_pb2.TrainSentence,
    ]
    GetParagraphs: grpc.UnaryStreamMultiCallable[
        nucliadb_protos.train_pb2.GetParagraphsRequest,
        nucliadb_protos.train_pb2.TrainParagraph,
    ]
    GetFields: grpc.UnaryStreamMultiCallable[
        nucliadb_protos.train_pb2.GetFieldsRequest,
        nucliadb_protos.train_pb2.TrainField,
    ]
    GetResources: grpc.UnaryStreamMultiCallable[
        nucliadb_protos.train_pb2.GetResourcesRequest,
        nucliadb_protos.train_pb2.TrainResource,
    ]
    GetOntology: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.GetLabelsRequest,
        nucliadb_protos.writer_pb2.GetLabelsResponse,
    ]
    GetEntities: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.GetEntitiesRequest,
        nucliadb_protos.writer_pb2.GetEntitiesResponse,
    ]
    GetOntologyCount: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.train_pb2.GetLabelsetsCountRequest,
        nucliadb_protos.train_pb2.LabelsetsCount,
    ]

class TrainServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetInfo(
        self,
        request: nucliadb_protos.train_pb2.GetInfoRequest,
        context: grpc.ServicerContext,
    ) -> nucliadb_protos.train_pb2.TrainInfo: ...
    @abc.abstractmethod
    def GetSentences(
        self,
        request: nucliadb_protos.train_pb2.GetSentencesRequest,
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[nucliadb_protos.train_pb2.TrainSentence]: ...
    @abc.abstractmethod
    def GetParagraphs(
        self,
        request: nucliadb_protos.train_pb2.GetParagraphsRequest,
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[nucliadb_protos.train_pb2.TrainParagraph]: ...
    @abc.abstractmethod
    def GetFields(
        self,
        request: nucliadb_protos.train_pb2.GetFieldsRequest,
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[nucliadb_protos.train_pb2.TrainField]: ...
    @abc.abstractmethod
    def GetResources(
        self,
        request: nucliadb_protos.train_pb2.GetResourcesRequest,
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[nucliadb_protos.train_pb2.TrainResource]: ...
    @abc.abstractmethod
    def GetOntology(
        self,
        request: nucliadb_protos.writer_pb2.GetLabelsRequest,
        context: grpc.ServicerContext,
    ) -> nucliadb_protos.writer_pb2.GetLabelsResponse: ...
    @abc.abstractmethod
    def GetEntities(
        self,
        request: nucliadb_protos.writer_pb2.GetEntitiesRequest,
        context: grpc.ServicerContext,
    ) -> nucliadb_protos.writer_pb2.GetEntitiesResponse: ...
    @abc.abstractmethod
    def GetOntologyCount(
        self,
        request: nucliadb_protos.train_pb2.GetLabelsetsCountRequest,
        context: grpc.ServicerContext,
    ) -> nucliadb_protos.train_pb2.LabelsetsCount: ...

def add_TrainServicer_to_server(servicer: TrainServicer, server: grpc.Server) -> None: ...
