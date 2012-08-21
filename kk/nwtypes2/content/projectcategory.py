from zope.interface import implements
from zope.component import adapts
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content import folder, document
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from kk.nwtypes2.interfaces import IProjectCategory
from kk.nwtypes2.config import PROJECTNAME
from Products.ATContentTypes.configuration import zconf

ProjectCategorySchema = folder.ATFolderSchema.copy()
class ProjectCategory(folder.ATFolder):
    """ category """
    
    implements(IProjectCategory)
    portal_type=meta_type="ProjectCategory"
    schema = ProjectCategorySchema

registerType(ProjectCategory, PROJECTNAME)